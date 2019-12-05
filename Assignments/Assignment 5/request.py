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
        # Pokemon, Ability, and Move objects
        self.results = []

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
               f"URLs: {self.urls}\n" \
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

    def handle_request(self, request_: Request) -> None:
        """
        Write the search term(s) to request.search_terms.
        :param request_: Request
        :return: None
        """
        print("FileExtensionHandler running...")

        # Open file and parse multiple search terms
        if request_.string.endswith(".txt"):
            with open(request_.string, 'r') as file:
                request_.search_terms = list(file)
                request_.search_terms = [
                    term.strip('\n ').lower().replace(' ', '-')
                    for term in request_.search_terms]
        else:
            # Store the string input into request.search_terms
            request_.search_terms.append(request_.string)

        print(f"File Extension, request_.search_terms:\n"
              f"{request_.search_terms}")

        if self.next_handler is None:
            return
        return self.next_handler.handle_request(request_)


class HttpHandler(BasePokedexHandler):

    async def handle_request(self, request_: Request) -> None:
        """
        Create the URLs associated with the original query/queries.
        :param request_: Request
        :return: None
        """
        print("HttpHandler running...")
        api_manager = api.APIManager()
        request_.json = await api_manager.open_session(request_)

        if self.next_handler is None:
            return
        return self.next_handler.handle_request(request_)


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
        Convert list of JSON into specific objects and append to
        request.results.
        :param request_: Request
        :return: None
        """
        print("JsonHandler running...")
        self._mode_dict.get(request_.mode)(request_)

    def get_pokemon(self, request_: Request) -> None:
        """
        Convert JSON to Pokemon object
        :return: Pokemon
        """
        for json in request_.json:
            pokemon = p.Pokemon(json["name"], json["id"], json["height"],
                                json["weight"], json["stats"], json["types"],
                                json["abilities"], json["moves"])
            request_.results.append(pokemon)

        for result in request_.results:
            print(result)

    def get_ability(self, request_: Request) -> None:
        """
        Convert JSON to Ability object
        :return: Ability
        """
        for json in request_.json:
            ability = p.Ability(json["name"], json["id"], json["generation"],
                                json["effect_entries"][0]["effect"],
                                json["effect_entries"][0]["short_effect"],
                                json["pokemon"])
            request_.results.append(ability)

        for result in request_.results:
            print(result)

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

        for result in request_.results:
            print(result)


def main(request: Request):
    print(request)


if __name__ == "__main__":
    request = RequestManager.setup_cli_request()
    main(request)
