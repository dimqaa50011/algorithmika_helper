from pathlib import Path

from environs import Env

BASE_DIR = Path(__file__).resolve().parent

env = Env()
env.read_env(BASE_DIR / '.env')


BOT_TOKEN = env.str('BOT_TOKEN')
USE_REDIS = env.bool('USE_REDIS')
ROOT_DJANGO_API = env.str('ROOT_DJANGO_API')
