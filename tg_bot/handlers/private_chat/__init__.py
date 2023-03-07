from .start import register_start_handlers
from .echo import register_echo_handler
from .before_lesson import register_before_lesson_handlers


def register_private_handlers(dp):
    register_start_handlers(dp)
    register_before_lesson_handlers(dp)
    
    register_echo_handler(dp) # регистрировать самым последним!!!
