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

    async def open_session(self, request_):
        tasks = []
        results = []
        stat_results = []
        ability_results = []
        move_results = []
        json_results = []
        subquery_results = []
        all_pokemon_results = []
        pokemon_results = []
        attribute_results = []
        temp = []

        stat_tasks = []
        ability_tasks = []
        move_tasks = []

        async with ClientSession() as session:
            if len(request_.stat_urls) < 1:
                urls = self.create_urls(request_)
                # Original queries in request
                for url in urls:
                    tasks.append(
                        asyncio.create_task(self.api_call(url, session)))
                # Results = JSON for original queries
                json_results += await asyncio.gather(*tasks)

                # Strip empty dictionaries for 404 API calls
                json_results = [result for result in json_results if
                                result is not {}]
            else:
                for pokemon_stats in request_.stat_urls:
                    for url in pokemon_stats:
                        tasks.append(asyncio.create_task(self.api_call(url,
                                                                       session)))
                    results += await asyncio.gather(*tasks)
                    stat_results.append(results)
                    tasks = []
                    results = []
                all_pokemon_results.append(stat_results)

                for pokemon_stats in request_.ability_urls:
                    for url in pokemon_stats:
                        tasks.append(asyncio.create_task(self.api_call(url,
                                                                       session)))
                    results += await asyncio.gather(*tasks)
                    ability_results.append(results)
                    tasks = []
                    results = []
                json_results.append(ability_results)

                for pokemon_stats in request_.move_urls:
                    for url in pokemon_stats:
                        tasks.append(asyncio.create_task(self.api_call(url,
                                                                       session)))
                    results += await asyncio.gather(*tasks)
                    move_results.append(results)
                    tasks = []
                    results = []
                json_results.append(move_results)

            return json_results
