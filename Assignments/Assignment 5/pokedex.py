from aiohttp import ClientSession
import request as r
import asyncio


class Pokedex:
    """
    Driver class that sets up chains of responsiblity.
    """

    def __init__(self):
        ex_file = r.FileExtensionHandler()
        ex_http = r.HttpHandler()
        ex_subquery = r.SubqueryUrlHandler()
        ex_http_sub = r.HttpHandler()
        # ex_json = r.JsonHandler()
        # ex_subquery = r.SubqueryHandler()
        # ex_http_sub = r.HttpHandler()
        # ex_print = r.OutputHandler()

        con_file = r.FileExtensionHandler()
        con_http = r.HttpHandler()
        con_json = r.JsonHandler()
        con_print = r.OutputHandler()

        self._expand_start_handler = ex_file
        ex_file.next_handler = ex_http
        ex_http.next_handler = ex_subquery
        ex_subquery.next_handler = ex_http_sub
        # ex_http.next_handler = ex_json
        # ex_json.next_handler = ex_subquery
        # ex_subquery.next_handler = ex_print
        # ex_http_sub.next_handler = ex_print

        self._concise_start_handler = con_file
        con_file.next_handler = con_http
        con_http.next_handler = con_json
        con_json.next_handler = con_print

    def execute_request(self, request):
        if request.is_expanded:
            return self._expand_start_handler.handle_request(request)
        else:
            return self._concise_start_handler.handle_request(request)


def main():
    request = r.RequestManager.setup_cli_request()
    driver = Pokedex()
    try:
        asyncio.run(driver.execute_request(request))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
