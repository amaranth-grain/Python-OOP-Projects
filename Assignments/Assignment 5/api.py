from aiohttp import ClientSession
import asyncio


class UrlGatherer:

    # TODO Fix Url gatherer and implement expanded/.;
    @classmethod
    def gather_urls(cls, json_list) -> list:
        stat_urls = []
        move_urls = []
        ability_urls = []
        pokemon_subqueries = []

        for json in json_list:
            for stat in json["stats"]:
                stat_urls.append(stat["stat"]["url"])

            for move in json["moves"]:
                move_urls.append(move["move"]["url"])

            for ability in json["abilities"]:
                ability_urls.append(ability["ability"]["url"])

            pokemon_subqueries.append(["***", stat_urls, move_urls,
                                       ability_urls])

        return pokemon_subqueries


class APIManager:

    def __init__(self):
        """
        Initialises API Manager.
        """
        self._base_url = "https://pokeapi.co/api/v2/{0}/{1}"

    def create_urls(self, request):
        """
        Loop through request.search_terms and create URLs for
        original query.  (Does not include subqueries.)
        :param request: Request
        :return: list of str
        """
        target_urls = []
        mode = request.mode.value
        for search in request.search_terms:
            target_urls.append(self._base_url.format(mode, search))
        return target_urls

    async def api_call(self, url, session: ClientSession):
        """
        Make API call for a single URL.
        :param url: str
        :param session: ClientSession
        :return: dict
        """
        response = await session.request(method="GET", url=url)
        if response.status == 200:
            try:
                return await response.json()
            except ValueError as e:
                print(e)
        return None

    async def open_session(self, request):
        tasks = []
        results = []
        async with ClientSession() as session:
            urls = self.create_urls(request)
            # Original queries in request
            for url in urls:
                tasks.append(
                    asyncio.create_task(self.api_call(url, session)))
            # Results = JSON for original queries
            results += await asyncio.gather(*tasks)

            # Strip empty dictionaries for 404 API calls
            results = [result for result in results if result is not {}]

            # if len(request.subquery_urls) < 1:
            #     urls = self.create_urls(request)
            #     # Original queries in request
            #     for url in urls:
            #         tasks.append(asyncio.create_task(self.api_call(url, session)))
            #     # Results = JSON for original queries
            #     results += await asyncio.gather(*tasks)
            #
            #     # Strip empty dictionaries for 404 API calls
            #     results = [result for result in results if result is not {}]
            # else:
            #     print("extend http handler")
            #     urls = self.create_urls(request)
            #     # Original queries in request
            #     for url in urls:
            #         tasks.append(
            #             asyncio.create_task(self.api_call(url, session)))
            #     # Results = JSON for original queries
            #     results += await asyncio.gather(*tasks)
            #
            #     # Strip empty dictionaries for 404 API calls
            #     results = [result for result in results if result is not {}]
            return results


