from jinja2 import Environment, FileSystemLoader

from config import BASE_DIR
from schemas.course import OutCourseSchema
from schemas.student import ListStudentSchema


jinja_env = Environment(
    enable_async=True,
    loader=FileSystemLoader([BASE_DIR / 'templates'])
) 


async def get_report_template(course: OutCourseSchema, students: ListStudentSchema):
    template = jinja_env.get_template('report')
    return await template.render_async({'course': course, 'students': students.students})