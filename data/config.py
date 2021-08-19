from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env("./.env.dev.local")

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = []  # env.list("ADMINS")  # Тут у нас будет список из админов

BASE_URL = env.str('BASE_URL')  # Webhook domain
WEBHOOK_BOT_PATH = f'/v1/webhook/bot/{BOT_TOKEN}'
WEBHOOK_BOT_URL = f'{BASE_URL}{WEBHOOK_BOT_PATH}'

CERT_PATH = env.str('WEBHOOK_SSL_CERT')


admins = []

ip = {
    'db':    '',
    'redis': '',
}

mysql_info = {
    'host':     '',
    'user':     '',
    'password': '',
    'db':       '',
    'maxsize':  5,
    'port':     3306,
}

aiogram_redis = {
    'host':     ip['redis'],
    'password': ''
}

redis = {
    'address':  (ip['redis'], 6379),
    'password': '',
    'encoding': 'utf8'
}
