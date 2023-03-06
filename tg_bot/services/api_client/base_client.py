from enum import Enum

import aiohttp

from config import ROOT_DJANGO_API


class AllowedMethods(Enum):
    GET: str = 'GET'
    POST: str = 'POST'
    PUT: str = 'PUT'
    PATCH: str = 'PATCH'
    DELETE: str = 'DELETE'


class BaseApiClient:
    def __init__(self) -> None:
        self.ROOT_URL = ROOT_DJANGO_API

    async def handler(self, method: AllowedMethods, url: str, **kwargs):
        curr_url = await self._get_current_url(url)
        return await self._perform_request(method, curr_url, **kwargs)

    async def _get_current_url(self, path: str):
        return '{}{}'.format(self.ROOT_URL, path.lstrip('/'))

    async def _perform_request(self, method: AllowedMethods, url: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            response = await session.request(method.value, url, **kwargs)
        if response.ok:
            return await response.json()
