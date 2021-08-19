"""Module to declare handlers to start survey."""
from aiogram import types
from contracts import contract
from aiogram.dispatcher.storage import FSMContext


@contract
async def initiate_survey(call: types.CallbackQuery, state: FSMContext):
    """Callback handler of the inline button to start survey

    :param call: callback instance caused by the inline button
    :type call: types.CallbackQuery
    """
    # TODO set state "Survey"
    # set survey response
    # set_data to this state: survey_response_id: List[{question_id}, ...]
    # send first question, based on its type (another function)
    pass


@contract
async def initiate_survey_error(call: types.CallbackQuery, state: FSMContext):
    """Callback handler of the inline button to send message about finishing
    previous survey

    :param call: callback instance caused by the inline button
    :type call: types.CallbackQuery
    """
    # TODO send message about finishing previous survey


@contract
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
