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
    # keyboard to get contact
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона",
                                        request_contact=True)
    keyboard.add(button_phone)
    await msg.bot.send_message(msg.from_user.id,
                               "Отправьте свой номер телефона",
                               reply_markup=keyboard)
    await state.set_state("telephone_state")


@contract
async def get_contact(msg: types.Message, state: FSMContext):
    """Handler to get telephone number

    :param msg: Message instance caused by sending contact
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    if msg.contact.phone_number is not None:
        print(msg.contact.phone_number)
        keyboard = types.ReplyKeyboardRemove()
        await msg.bot.send_message(msg.from_user.id,
                                   "Вы успешно отправили свой номер",
                                   reply_markup=keyboard)
        await state.set_state("initial_state")
