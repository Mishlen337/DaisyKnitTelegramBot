"""Package to declare handlers for a survey and its respones"""
from aiogram import Dispatcher
from .survey import initiate_survey


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(initiate_survey, state="initial_state",
                                       is_survey=True)
