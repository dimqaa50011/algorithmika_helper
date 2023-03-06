from .start import register_start_handlers
from .echo import register_echo_handler


def register_private_handlers(dp):
    register_start_handlers(dp)
    
    register_echo_handler(dp) # регистрировать самым последним!!!
