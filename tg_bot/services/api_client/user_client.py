from typing import Union, Optional, List, Dict, AsyncIterable

from .base_client import BaseApiClient, AllowedMethods
from schemas.user import CreateUserSchema, OutUserSchema, ListUserSchema, UpdateUserSchema


class UserApiClient(BaseApiClient):
    def __init__(self):
        super().__init__()
        self.USER_PATH_URL = 'user/'

    async def create_item(self, data: CreateUserSchema) -> Optional[OutUserSchema]:
        response = await self.handler(
            method=AllowedMethods.POST,
            url=self.USER_PATH_URL,
            data=data.dict()
        )
        return response if response is None else OutUserSchema(**response)

    async def get_item(self, tg_id: Union[str, int]) -> Optional[OutUserSchema]:
        response = await self.handler(
            AllowedMethods.GET,
            url=f'{self.USER_PATH_URL}{str(tg_id).lstrip("/")}'
        )
        return response if response is None else OutUserSchema(**response)

    async def get_all_items(self) -> ListUserSchema:
        response = await self.handler(
            AllowedMethods.GET,
            url=f'{self.USER_PATH_URL}list/'
        )
        return await self._get_list_user_schema(response)

    async def update_item(self, tg_id: int, data: UpdateUserSchema) -> OutUserSchema:
        response = await self.handler(
            AllowedMethods.PATCH,
            url=f'{self.USER_PATH_URL}{str(tg_id)}/',
            data=data.dict()
        )
        return response if response is None else OutUserSchema(**response)

    async def _get_list_user_schema(self, data: List[Dict]) -> ListUserSchema:
        users = []
        async for user in self._get_out_user_schema(data):
            users.append(
                OutUserSchema(
                    first_name=user.get('first_name'),
                    last_name=user.get('last_name'),
                    tg_username=user.get('tg_username'),
                    tg_id=user.get('tg_id')
                )
            )
        return ListUserSchema(users=users)

    @staticmethod
    async def _get_out_user_schema(data: List[Dict]) -> AsyncIterable:
        for item in data:
            yield item


