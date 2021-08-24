"""Package to declare handlers for a survey and its respones"""
from aiogram import Dispatcher
from aiogram.types.callback_query import CallbackQuery
from .survey import initiate_survey
from .response_quiz import QuizResponse
from .response_callback import ResponseCallback
from .response_message import ResponseMessage
from aiogram.utils.callback_data import CallbackData


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(ResponseCallback().get_response,
                                       state="survey_state")
    dp.register_message_handler(ResponseMessage().get_response,
                                state="survey_state")
    dp.register_callback_query_handler(initiate_survey, state="initial_state",
                                       is_survey=True)
    dp.register_poll_answer_handler(QuizResponse(dp).get_response)
