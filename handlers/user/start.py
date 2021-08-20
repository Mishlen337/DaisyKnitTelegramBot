from aiogram import types
from aiogram.dispatcher.storage import FSMContext


async def bot_start(msg: types.Message, state: FSMContext):
    await msg.answer(f'Привет, {msg.from_user.full_name}!')
    await state.set_state('initial_state')
