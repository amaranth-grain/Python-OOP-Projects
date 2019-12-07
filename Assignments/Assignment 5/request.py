from enum import Enum
import api
import pokemon as p
from abc import ABC, abstractmethod
from argparse import ArgumentParser


class PokedexMode(Enum):
    """
    Modes for querying Pokedex.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class FileExtensionError(Exception):
    """
    Error thrown when the file extension is incorrect.
    """

    def __init__(self, path):
        super().__init__(f"Your file path '{path}' does not end with the "
                         f".txt file extension.")
        self.path = path


class ZeroResultsError(Exception):
    """
    Error thrown when zero API calls were made successfully.
    """

    def __init__(self):
        super().__init__(f"No API calls were made successfully. Check your "
                         f"input and/or Pokedex mode.")


class Request:
    """
    Represent a user request for querying PokeAPI.
    """

    def __init__(self):
        # pokemon, ability, or move
        self.mode = None
        # id, name, or file path.
        self.string = None
        # Whether query is an expanded search
        self.is_expanded = False
        # Output file path
        self.output_path = None
        # Where multiple search terms are stored
        self.search_terms = []
        # Where JSON from queries are stored
        self.json = []
        # Where subquery urls are stored
        self.subquery_urls = []
        # Pokemon, Ability, and Move objects
        self.results = []
        self.stat_urls = []
        self.ability_urls = []
        self.move_urls = []

    def __str__(self):
        """
        String representation of Request
        :return: String
        """
        return f"Mode: {self.mode}\n" \
               f"String: {self.string}\n" \
               f"Is Expanded: {self.is_expanded}\n" \
               f"Output Path: {self.output_path}\n" \
               f"Search terms: {self.search_terms}\n" \
               f"Results: {self.results}\n"


class RequestManager:
    """
    Parse command line args into a Request object.
    """

    @staticmethod
    def setup_cli_request() -> Request:
        parser = ArgumentParser()
        parser.add_argument("mode",
                            help="Mode in which the Pokedex is opened. Can "
                                 "be Pokemon, Ability, or MOve")
        parser.add_argument("string", type=str.lower,
                            help="The search input. Either a Pokemon ID, Pokemon "
                                 "name, or text file path.")
        parser.add_argument("-e", "--expanded", action="store_true",
                            help="Determine whether subqueries are performed "
                                 "on expandable attributes.  By default "
                                 "expanded is set to false.")
        parser.add_argument("-o", "--output", default="print",
                            help="The output of the program.  Set to PRINT "
                                 "by default, but can be set to .txt file")
        try:
            args = parser.parse_args()
            print(f"args: {args.__dict__}")
            cli_request = Request()
            cli_request.mode = PokedexMode(args.mode.lower())
            cli_request.string = args.string.replace(' ', '-')
            cli_request.is_expanded = args.expanded
            cli_request.output_path = args.output
            return cli_request
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()


class BasePokedexHandler(ABC):
    """
    Abstract base handler that all Pokedex handlers inherit from.
    """

    def __init__(self, next_handler=None) -> None:
        """
        Initialises a Pokedex handler and sets up the next Handler.
        :param next_handler: BasePokedexHandler
        """
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request_: Request) -> None:
        """
        Handles the command line Request.
        :param request_: Request
        :return: None
        """
        pass

    @property
    def next_handler(self):
        """
        Returns the next Pokedex handler.
        :return: BasePokedexHandler
        """
        return self._next_handler

    @next_handler.setter
    def next_handler(self, next_handler):
        """
        Sets the next handler in the chain.
        :param handler: BasePokedexHandler
        :return: None
        """
        self._next_handler = next_handler


class FileExtensionHandler(BasePokedexHandler):

    async def handle_request(self, request_: Request) -> None:
        """
        Write the search term(s) to request.search_terms.
        :param request_: Request
        :return: None
        """
        print("FileExtensionHandler running...")
        if request_.string.endswith(".txt"):
            with open(request_.string, 'r') as file:
                request_.search_terms = list(file)
                request_.search_terms = [
                    term.strip('\n ').lower().replace(' ', '-')
                    for term in request_.search_terms]
        else:
            request_.search_terms.append(request_.string)

        if self.next_handler is None:
            return
        return await self.next_handler.handle_request(request_)


class HttpHandler(BasePokedexHandler):
    async def handle_request(self, request_: Request) -> None:
        """
        Create the URLs associated with the original query/queries.
        Make API calls based on these URLs, and store in request_.json
        :param request_: Request
        :return: None
        """
        print("HttpHandler running...")
        api_manager = api.APIManager()
        request_.json = await api_manager.open_session(request_)

        request_.json = [json for json in request_.json if
                         json is not None]

        if self.next_handler is None:
            return
        return await self.next_handler.handle_request(request_)


class SubqueryUrlHandler(BasePokedexHandler):

    async def handle_request(self, request_: Request) -> None:
        """
        Grab the subquery urls and store in request_.subquery_urls
        :param request_: Request
        :return: None
        """
        print("SubqueryUrlHandler running...")
        stat = []
        ability = []
        move = []
        # [ stat[], ability[], move[] ]
        one_pokemon_urls = []

        for pokemon_json in request_.json:
            for i in range(len(pokemon_json['stats'])):
                stat.append(pokemon_json['stats'][i]['stat'][
                                           'url'])

            for a in pokemon_json['abilities']:
                ability.append(a['ability']['url'])

            for i in range(len(pokemon_json['moves'])):
                move.append(pokemon_json['moves'][i]['move']['url'])

            request_.stat_urls.append(stat)
            request_.ability_urls.append(ability)
            request_.move_urls.append(move)
            # one_pokemon_urls.append(stat)
            # one_pokemon_urls.append(ability)
            # one_pokemon_urls.append(move)
            # request_.subquery_urls.append(one_pokemon_urls)

            # Reset for the next Pokemon
            stat = []
            move = []
            ability = []
            one_pokemon_urls = []

        if self.next_handler is None:
            return
        return await self.next_handler.handle_request(request_)


class JsonHandler(BasePokedexHandler):

    def __init__(self):
        super().__init__()
        self._mode_dict = {
            PokedexMode.POKEMON: self.get_pokemon,
            PokedexMode.ABILITY: self.get_ability,
            PokedexMode.MOVE: self.get_move
        }

    def handle_request(self, request_: Request) -> None:
        """
        Convert list of JSON into specific objects and append to results.
        :param request_: Request
        :return: None
        """
        print("JsonHandler running...")
        self._mode_dict.get(request_.mode)(request_)
        if self.next_handler is None:
            return
        return self.next_handler.handle_request(request_)

    def get_pokemon(self, request_: Request) -> None:
        """
        Convert JSON to Pokemon object
        :return: Pokemon
        """
        for json in request_.json:
            # Create stats object
            base_list = []
            for stat in json["stats"]:
                name = stat["stat"]["name"]
                base_stats = stat["base_stat"]
                url = stat["stat"]["url"]
                base_list.append(p.BaseStats(name, base_stats, url))
            stats = p.Stats(base_list[0], base_list[1], base_list[2],
                            base_list[3], base_list[4], base_list[5])

            # Create list of Abilities
            abilities = []
            for i in range(len(json["abilities"])):
                name = json["abilities"][i]["ability"]["name"]
                url = json["abilities"][i]["ability"]["url"]
                abilities.append(p.Ability(name=name, url=url))

            # Create list of Moves
            moves = []
            for i in range(len(json["moves"])):
                name = json["moves"][i]["move"]["name"]
                level = json["moves"][i]["version_group_details"][0][
                    "level_learned_at"]
                move_url = json["moves"][i]["move"]["url"]
                moves.append(p.Move(name=name, level=level, url=move_url))
                # setattr(key, value)

            # Create Pokemon
            pokemon = p.Pokemon(json["name"], json["id"], json["height"],
                                json["weight"], stats, json["types"],
                                abilities, moves)
            request_.results.append(pokemon)

    def get_ability(self, request_: Request) -> None:
        """
        Convert JSON to Ability object
        :return: Ability
        """
        for json in request_.json:
            ability = p.Ability(json["name"], json["id"],
                                json["generation"],
                                json["effect_entries"][0]["effect"],
                                json["effect_entries"][0]["short_effect"],
                                json["pokemon"])
            request_.results.append(ability)

    def get_move(self, request_: Request) -> None:
        """
        Convert JSON to Move object
        :return: Move
        """
        for json in request_.json:
            move = p.Move(json["name"], json["id"], json["generation"]["name"],
                          json["accuracy"], json["pp"], json["power"],
                          json["type"], json["damage_class"],
                          json["effect_entries"][0]["short_effect"])
            request_.results.append(move)


class JsonSubqueryHandler(BasePokedexHandler):

    def handle_request(self, request_: Request) -> None:
        """
        Convert list of JSON into specific objects and append to results.
        :param request_: Request
        :return: None
        """
        print("JsonHandler running...")
# class SubqueryHandler(BasePokedexHandler):
#
#     def handle_request(self, request_: Request) -> None:
#         """
#         For expanded queries, grab subquery URLs.
#         :param request_: Request
#         :return: None
#         """
#         print("SubqueryHandler running...")
#         all_urls = self.get_all_subquery_urls(request_)
#         request_.subquery_urls = all_urls
#         if self.next_handler is None:
#             return
#         return self.next_handler.handle_request(request_)
#
#     def get_all_subquery_urls(self, request_):
#         num_results = len(request_.results)
#         # [ stats[], ability[], move[] ]
#         one_pokemon_urls = []
#         # [ [ stats[], ability[], move[] ], [ stats[], ability[], move[] ] ]
#         all_pokemon_urls = []
#         for i in range(num_results):
#             one_pokemon_urls.clear()
#             one_pokemon_urls.append(self.get_stat_urls(i, request_))
#             one_pokemon_urls.append(self.get_ability_urls(i, request_))
#             one_pokemon_urls.append(self.get_move_urls(i, request_))
#             all_pokemon_urls.append(one_pokemon_urls)
#         return all_pokemon_urls
#
#     def get_stat_urls(self, i, request_):
#         """
#         Get Stats URLs for one expanded Pokemon.
#         :param i: index int
#         :param request_: Request
#         :return: list of stat urls
#         """
#         return request_.results[i].stats.get_stats_urls()
#
#     def get_ability_urls(self, i, request_):
#         """
#         Get Ability URLs for one expanded Pokemon.
#         :param i: index int
#         :param request_: Request
#         :return: list of Ability urls
#         """
#         abilities_url = []
#         for ability in request_.results[i].abilities:
#             abilities_url.append(ability.url)
#         return abilities_url
#
#     def get_move_urls(self, i, request_):
#         """
#         Get Move URLs for one expanded Pokemon
#         :param i: index int
#         :param request_: Request
#         :return: list of Move urls
#         """
#         move_urls = []
#         for move in request_.results[i].moves:
#             move_urls.append(move.url)
#         return move_urls


class OutputHandler(BasePokedexHandler):

    def handle_request(self, request_: Request) -> None:
        """
        Print request.results.
        :param request_: Request
        :return: None
        """
        print("OutputHandler running...")
        if request_.output_path.lower() == "print":
            for result in request_.results:
                print(result)
            if not request_.results:
                raise ZeroResultsError
        elif request_.output_path.endswith(".txt"):
            with open(request_.output_path, "w+") as file:
                for result in request_.results:
                    file.write(result.__str__())
        else:
            raise FileExtensionError(request_.output_path)


def main(request: Request):
    print(request)


if __name__ == "__main__":
    request = RequestManager.setup_cli_request()
    main(request)
