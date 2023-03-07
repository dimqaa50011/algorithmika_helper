from typing import List, Dict, AsyncIterable

from .base_client import BaseApiClient, AllowedMethods
from schemas.course import OutCourseSchema, ListCourseSchema


class CourseClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__()
        self.COURSE_PATH_URL = 'course/'
    
    async def get_all_items(self):
        COURSE_LIST_URL = f'{self.COURSE_PATH_URL}list/'
        response = await self.handler(
            method=AllowedMethods.GET,
            url=COURSE_LIST_URL
        )
        courses = []
        async for course in self._async_iterator(response):
            courses.append(
                OutCourseSchema(
                    id=course.get('id'),
                    start_date=course.get('start_date'),
                    end_date=course.get('end_date'),
                    start_time=course.get('start_time'),
                    backoffice_link=course.get('backoffice_link'),
                    title=course.get('title')
                )
            )
        return ListCourseSchema(courses=courses)
    
    async def get_item(self, pk: int):
        COURSE_URL = f'{self.COURSE_PATH_URL}{pk}'
        response = await self.handler(
            method=AllowedMethods.GET,
            url=COURSE_URL
        )
        return OutCourseSchema(**response)

    async def _async_iterator(self, data: List[Dict]) -> AsyncIterable:
        for item in data:
            yield item
        

