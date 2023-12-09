from aiogram import types
from aiogram.dispatcher.storage import FSMContext



async def bot_start(msg: types.Message, state: FSMContext):
    """Handler to register user in his/her first entry

    :param msg: Message instance caused by received message
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    await msg.answer(f'Привет, {msg.from_user.full_name}!')
    # Set keyboard to get contact
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона",
                                        request_contact=True)
    keyboard.add(button_phone)
    await msg.bot.send_message(msg.from_user.id, "Отправьте номер телефона",
                               reply_markup=keyboard)
    await state.set_state("telephone_state")


async def bot_start_error(msg: types.Message, state: FSMContext):
    """Handler to register bot start error

    :param msg: Message instance caused by received message
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    await msg.bot.send_message(msg.from_user.id, "Вы уже зарегистрированны в боте.")
    text = [
        'Список команд: ',
        '/help - Получить справку',
        '/survey - Начать опрос',
        '/finish - Завершить опрос',
    ]
    await msg.answer('\n'.join(text))
    await state.set_state("initial_state")
