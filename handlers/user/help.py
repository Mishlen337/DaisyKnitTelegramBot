from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from utils.misc import rate_limit


@rate_limit(5, 'help')
async def bot_help(msg: types.Message, state: FSMContext):
    text = [
        'Список команд: ',
        '/help - Получить справку',
        '/survey - Начать опрос',
        '/finish - Завершить опрос',
    ]
    await msg.answer('\n'.join(text))
