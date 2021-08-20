from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from contracts import contract


@contract
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
