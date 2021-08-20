from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from utils.misc import rate_limit


@rate_limit(5, 'help')
async def bot_help(msg: types.Message, state: FSMContext):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await msg.answer('\n'.join(text))
    await msg.answer_poll(question="smth",
                          options=[str(i+1) for i in range(10)],
                          is_anonymous=False)
