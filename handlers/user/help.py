from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from utils.misc import rate_limit

help_message = """
Список команд: 
/help - Получить справку
/start - Оформить новый заказ
/finish - Завершить заказ/опрос

Где забирать заказ? 
⚓Точка на Гугл-карте: https://maps.app.goo.gl/8d8j34w8iNsLBgCy7.

Во сколько забирать заказ?
🕢 На зимнее время 08.00-08.30.
🌱Если по какой то причине не можете забрать заказ вовремя, пожалуйста, заранее сообщите об этом и я по-возможности, попробую решить как вам получить заказ😊.
Также в утренние часы доступна доставка по Бару от 3 евро.

☎️ Меня зовут Анна, мой номер 068715337, мой телеграмм @anjaglebova
Можете мне писать или звонить, если у вас возникнут вопросы или вы хотите изменить заказ.

Ссылка на телеграмм канал, где появляется актуальная информация: https://t.me/foreljbar

Ps.👛Возьмите, по-возможности, пожалуйста, мелкие деньги, монетки, чтобы не было проблем со сдачей"""

@rate_limit(5, 'help')
async def bot_help(msg: types.Message, state: FSMContext):
    await msg.answer(help_message)

async def bot_message(msg: types.Message, state: FSMContext):
    message = "Для оформления заказа введите команду /start"
    await msg.answer(message)
