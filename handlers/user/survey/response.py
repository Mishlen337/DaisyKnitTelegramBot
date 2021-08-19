"""Modules to declare handlers for surveys respones."""

from typing import Union
from contracts import contract
from aiogram.types import CallbackQuery, Message, PollAnswer
from aiogram.dispatcher.storage import FSMContext


@contract
async def get_response(response: Union[CallbackQuery, Message, PollAnswer],
                       state: FSMContext):
    """Response handler to get response

    :param response: Response to a question instance
    :type response: Union[CallbackQuery, Message, PollAnswer]
    :param state: State instance with survey and question data
    :type state: FSMContext
    """
    # TODO get name of the survey from state data
    # Get survey response instance
    # Get Survey instance
    # Get question to a survey id from state data(pop)
    # Save answer in database
    # if list of question id is empty - notify SurveyResponse
    # Get next question to a survey id from state data
    # else send next question using type (another function)
    pass


@contract
async def get_response_error(response: Union[CallbackQuery,
                                             Message,
                                             PollAnswer],
                             state: FSMContext):
    """Response handler to send message about finishing
    previous survey

    :param response: Response to a question instance
    :type response: Union[CallbackQuery, Message, PollAnswer]
    :param state: State instance with survey and question data
    :type state: FSMContext
    """
    # TODO send message to finish previous survey
    pass


async def log_response(user_id: str, response: str):
    """Log response to a question

    :param user_id: user id
    :type user_id: str
    :param response: response to a question
    :type response: str
    """
    # TODO
    # Сделать pop
    # Положить ответ в БД.
    # Посмотреть пуст ли список вопросов
    # Да - отправить в MindBox
    # Нет - оптравить новый вопрос с учетом типа
    pass
