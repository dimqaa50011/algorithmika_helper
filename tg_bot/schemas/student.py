from typing import List

from pydantic import BaseModel


class StudentBaseSchema(BaseModel):
    first_name: str
    last_name: str
    parent_phone: str
    is_presence: bool
    course: int


class OutStudentSchema(StudentBaseSchema):
    id: int


class UpdateStudentSchema(OutStudentSchema):
    pass


class ListStudentSchema(BaseModel):
    students: List[OutStudentSchema]
