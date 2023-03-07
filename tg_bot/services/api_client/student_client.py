from typing import List, Dict, AsyncIterable

from .base_client import BaseApiClient, AllowedMethods
from schemas.student import OutStudentSchema, UpdateStudentSchema, ListStudentSchema


class StudentClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__()
        self.STUDENT_PATH_URL = 'student/'
    
    async def get_students_by_course(self, pk: int, report: bool = False) -> ListStudentSchema:
        if report:
            CURRENT_STUDENT_URL = f'{self.STUDENT_PATH_URL}report/{pk}'
        else:    
            CURRENT_STUDENT_URL = f'{self.STUDENT_PATH_URL}list/{pk}'
        response = await self.handler(
            method=AllowedMethods.GET,
            url=CURRENT_STUDENT_URL
        )

        students = []
        async for student in self._async_iterator(response):
            students.append(
                OutStudentSchema(
                    id=student.get('id'),
                    first_name=student.get('first_name'),
                    last_name=student.get('last_name'),
                    parent_phone=student.get('parent_phone'),
                    is_presence=student.get('is_presence'),
                    course=student.get('course')
                )
            )
        return ListStudentSchema(students=students)
    
    async def get_item(self, pk: int) -> OutStudentSchema:
        CURRENT_STUDENT_URL = '{}{}'.format(self.STUDENT_PATH_URL, pk)
        response = await self.handler(
            method=AllowedMethods.GET,
            url=CURRENT_STUDENT_URL,
        )
        return OutStudentSchema(**response)
    
    async def update_item(self, pk: int, data: UpdateStudentSchema) -> OutStudentSchema:
        CURRENT_STUDENT_URL = '{}{}'.format(self.STUDENT_PATH_URL, pk)
        response = await self.handler(
            method=AllowedMethods.PATCH,
            url=CURRENT_STUDENT_URL,
            data=data.dict()
        )
        return OutStudentSchema(**response)
    
    async def _async_iterator(self, data: List[Dict]) -> AsyncIterable:
        for item in data:
            yield item
    
        

