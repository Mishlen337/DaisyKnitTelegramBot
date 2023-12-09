"""Package to declare handlers for a survey and its respones"""
from aiogram import Dispatcher

from . import survey
from . import response_callback
from . import response_message
# from .response_quiz import QuizResponse
from filters.survey.response import ResponseTypeValidFilter, ResponseCallbackValidFilter


def setup(dp: Dispatcher):
    dp.register_message_handler(response_message.finish,
                                commands='finish', state="survey_state")

    dp.register_message_handler(response_message.get_response_error,
                                ResponseTypeValidFilter(False, dp),
                                state="survey_state")

    dp.register_message_handler(response_message.ResponseMessage(dp).get_response,
                                ResponseTypeValidFilter(True, dp),
                                state="survey_state")

    dp.register_callback_query_handler(response_callback.ResponseCallback(dp).get_response,
                                       ResponseTypeValidFilter(True, dp), ResponseCallbackValidFilter(True, dp),
                                       state="survey_state")

    dp.register_callback_query_handler(response_callback.ResponseCallback(dp).get_response_error,
                                       ResponseCallbackValidFilter(False, dp),
                                       state="survey_state")

    # dp.register_poll_answer_handler(QuizResponse(dp).get_response)
    dp.register_callback_query_handler(survey.initiate_survey, state="initial_state",
                                       is_survey=True)
