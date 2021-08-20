from aiogram import Dispatcher
from states.user.states import DaisyKnitStates as DK

from .help import bot_help
from .start import bot_start
# from poll import poll_handler


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, commands="start")
    dp.register_message_handler(bot_help, commands="help",
                                state='initial_state')
    # dp.register_poll_answer_handler(poll_handler)
