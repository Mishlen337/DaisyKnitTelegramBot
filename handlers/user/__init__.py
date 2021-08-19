from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .help import bot_help
from .start import bot_start
from .poll import poll_handler


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_poll_answer_handler(poll_handler)
