from datetime import date, time
from typing import List

from pydantic import BaseModel


class CourseBaseSchema(BaseModel):
    start_date: date
    end_date: date
    start_time: time
    backoffice_link: str
    title: str


class OutCourseSchema(CourseBaseSchema):
    id: int


class ListCourseSchema(BaseModel):
    courses: List[OutCourseSchema] 