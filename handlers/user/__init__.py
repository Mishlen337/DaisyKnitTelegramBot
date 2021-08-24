from aiogram import Dispatcher
from .help import bot_help
from .start import bot_start
from .get_contact import get_contact
from . import survey


def setup(dp: Dispatcher):
    survey.setup(dp)
    dp.register_message_handler(bot_start, commands="start",
                                is_registered=False)
    dp.register_message_handler(bot_help, commands="help",
                                state="initial_state")
    dp.register_message_handler(get_contact, content_types="contact",
                                state="telephone_state")
    # dp.register_poll_answer_handler(poll_handler)
