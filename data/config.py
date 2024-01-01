import json
from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env("./.env")

# BOT settings
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str

BASE_URL = env.str('BASE_URL')  # Webhook domain
WEBHOOK_BOT_PATH = f'/bot/webhook/'
WEBHOOK_BOT_URL = f'{BASE_URL}{WEBHOOK_BOT_PATH}'

ADMIN = env.int('ADMIN')
MANAGER_TEL_IDS = env.list('MANAGER_TEL_IDS', subcast=int)
admins = [ADMIN, ]
SURVEY_NAMES = env.list('SURVEY_NAMES')
print(SURVEY_NAMES)
# MySQL settings
MYSQL_HOST = env.str('MYSQL_HOST')
MYSQL_DATABASE = env.str('MYSQL_DATABASE')
MYSQL_USER = env.str('MYSQL_USER')
MYSQL_PASSWORD = env.str('MYSQL_PASSWORD')

# Redis settings
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PASSWORD = env.str('REDIS_PASSWORD')


ip = {
    'db':    MYSQL_HOST,
    'redis': REDIS_HOST,
}

mysql_info = {
    'host':     ip['db'],
    'user':     MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'db':       MYSQL_DATABASE,
    'port':     3306,
}

aiogram_redis = {
    'host':     ip['redis'],
    'port':     6379,
    'password': REDIS_PASSWORD,
    'db':       10
}

redis = {
    'address':  (ip['redis'], 6379),
    'password': REDIS_PASSWORD,
    'encoding': 'utf8'
}
