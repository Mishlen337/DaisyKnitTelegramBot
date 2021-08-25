"""Package to declare handlers for a survey and its respones"""
from aiogram import Dispatcher
from aiogram.dispatcher import filters
from aiogram.types.callback_query import CallbackQuery
from .survey import initiate_survey
from .response_quiz import QuizResponse
from . import response_callback
from . import response_message
from filters.survey.response import ResponseValidFilter


def setup(dp: Dispatcher):
    dp.register_message_handler(response_message.finish,
                                commands='finish', state="survey_state")

    dp.register_message_handler(response_message.get_response_error,
                                ResponseValidFilter(False, dp),
                                state="survey_state")

    dp.register_message_handler(response_message.ResponseMessage().get_response,
                                ResponseValidFilter(True, dp),
                                state="survey_state")

    dp.register_callback_query_handler(response_callback.ResponseCallback().get_response,
                                       ResponseValidFilter(True, dp),
                                       state="survey_state")

    dp.register_poll_answer_handler(QuizResponse(dp).get_response)
    dp.register_callback_query_handler(initiate_survey, state="initial_state",
                                       is_survey=True)
