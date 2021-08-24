"""Module to declare handlers to start survey."""
from aiogram import types
from contracts import contract
from aiogram.dispatcher.storage import FSMContext
from utils.db_api.models.survey import Survey
from utils.db_api.models.user import User
from utils.db_api.models.survey_response import SurveyResponse
from .utils import send_next_question


async def initiate_survey(call: types.CallbackQuery, state: FSMContext):
    """Callback handler of the inline button to start survey

    :param call: callback instance caused by the inline button
    :type call: types.CallbackQuery
    """
    survey = Survey(call.data)
    await survey.set_info_db()
    user = User(call.from_user.id)
    await user.set_info_db()
    survey_response: SurveyResponse = await SurveyResponse.save(survey, user)
    # set survey response
    questions = await survey_response.survey.get_questions()
    await state.set_data({survey_response.id: questions})
    # set_data to this state: survey_response_id: List[{question_name}, ...]
    await send_next_question(call.bot, call.from_user.id, await state.get_data())
    await state.set_state("survey_state")
    # send first question, based on its type (another function)


async def initiate_survey_error(call: types.CallbackQuery, state: FSMContext):
    """Callback handler of the inline button to send message about finishing
    previous survey

    :param call: callback instance caused by the inline button
    :type call: types.CallbackQuery
    """
    # TODO send message about finishing previous survey
    pass


async def log_initiate_survey(survey_name: str, user_id: str):
    """"Logs starting survey

    :param survey_name: surveys name
    :type survey_name: str
    :param user_id: users id
    :type user_id: str
    """
    # TODO insert data to Redis.
    # data: {user_id}_survey: List[{question_id}_{survey_id}, ...]
    # logs question, based on its type (another function)
    pass
