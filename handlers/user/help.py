from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from utils.misc import rate_limit

help_message = """
Список команд: 
/help - Получить справку
/start - Оформить новую запись
/finish - Преждевременно закончить форму записи

Где проходит осмотр? 
⚓Точка на Гугл-карте: https://maps.app.goo.gl/UYmNetN6Fs3ocDee7.

☎️ Меня зовут Людмила, мой номер +382 68 361 489, мой телеграмм @ejkasan
Можете мне писать или звонить, если у вас возникнут вопросы или вы хотите отменить запись.

☎️ Для срочной записи звоните по номеру: +382 68 361 489

Ссылка на телеграмм канал, где появляется актуальная информация: https://t.me/VEYakovlev
"""

@rate_limit(5, 'help')
async def bot_help(msg: types.Message, state: FSMContext):
    await msg.answer(help_message)

async def bot_message(msg: types.Message, state: FSMContext):
    message = "Для оформления заказа введите команду /start"
    await msg.answer(message)
