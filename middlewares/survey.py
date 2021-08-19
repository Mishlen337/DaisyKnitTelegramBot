from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class PollMiddleWare(BaseMiddleware):
    def __init__(self):
        pass

    def on_pre_process_update(update: types.Update, data: dict):
        update.p

    def on_pre_process_poll(poll: types.PollAnswer):
        pass
