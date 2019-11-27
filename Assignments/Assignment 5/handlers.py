from argparse import ArgumentParser
from enum import Enum


class PokedexMode(Enum):
    """
    Modes for querying Pokedex.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Request:
    """
    Represent a CLI user
    """
    def __init__(self):
        # pokemon, ability, or move
        self._mode = None
        # id, or name
        self._query = None
        # file path
        self._input = None
        self._is_expanded = None
        self._output = None

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode

    @property
    def query(self):
        return self._query

    @query.setter


    @property
    def input(self):
        return self._input

    @property
    def is_expanded(self):
        return self._is_expanded

    @property
    def output(self):
        return self._output


    def __str__(self):
        """
        String representation of Request
        :return: String
        """
        return f"String: {self._query}\n" \
               f"Input file: {self._input}\n" \
               f"Is Expanded: {self._is_expanded}\n" \
               f"Output: {self._output}\n"


def setup_cli_request() -> Request:

    parser = ArgumentParser()
    parser.add_argument("mode", help="Mode in which the Pokedex is opened.")
    parser.add_argument("-q", "--query",
                        help="The search input. Either an id or a name.")
    parser.add_argument("-i", "--input",
                        help="The .txt file that needs to be "
                             "queried against PokeAPI.")
    parser.add_argument("-e", "--expanded", default="false",
                        help="Determine whether subqueries are performed "
                             "on expandable attributes.")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program.  Set to PRINT "
                             "by default, but can be set to .txt file")

    try:
        args = parser.parse_args()
        print(f"args: {args}")
        cli_request = Request()
        print(f"Pokemode: {PokedexMode(args.mode)}")
        cli_request._mode = PokedexMode(args.mode)
        print(f"cli request mode: {cli_request._mode}")
        cli_request._query = args.query
        cli_request._input = args.input
        cli_request._is_expanded = args.expanded
        cli_request._output = args.output
        return cli_request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


def main(request: Request):
    print(request)


if __name__ == "__main__":
    request = setup_cli_request()
    main(request)