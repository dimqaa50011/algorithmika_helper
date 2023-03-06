from typing import List

from pydantic import BaseModel, Field


class UserSchemaBase(BaseModel):
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    tg_username: str = Field(default=None)
    tg_id: int = Field(...)


class CreateUserSchema(UserSchemaBase):
    pass


class OutUserSchema(UserSchemaBase):
    pass


class UpdateUserSchema(OutUserSchema):
    pass


class ListUserSchema(BaseModel):
    users: List[OutUserSchema]