from aiogram import Dispatcher, types
from .help import bot_help
from .start import bot_start, get_contact
# from poll import poll_handler


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, commands="start")
    dp.register_message_handler(bot_help, commands="help",
                                state="initial_state")
    dp.register_message_handler(get_contact, content_types="contact",
                                state="telephone_state")
    # dp.register_poll_answer_handler(poll_handler)
