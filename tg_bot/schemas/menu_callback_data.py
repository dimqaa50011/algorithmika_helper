from pydantic import BaseModel, Field


class BaseMenuClallback(BaseModel):
    report: str = Field(default='0')
    course_id: str = Field(default='0')
    student_id: str = Field(default='0')


class CreateMenuCallback(BaseMenuClallback):
    level: str = Field(default='0')


class OutMenuCallback(BaseMenuClallback):
    pass
