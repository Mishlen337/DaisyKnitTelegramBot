"""Modules to declare handlers for surveys respones."""

from typing import Dict, Union, List
from contracts import contract
from aiogram.types import CallbackQuery, Message, PollAnswer
from aiogram.dispatcher.storage import FSMContext
from numpy import uint32
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.question import Question
from utils.db_api.models.response import Response
from data.events import responses_survey_manager
from .utils import send_next_question


# Union[CallbackQuery, Message, PollAnswer]
async def get_response(response: PollAnswer,
                       state: FSMContext):
    """Response handler to get response

    :param response: Response to a question instance
    :type response: Union[CallbackQuery, Message, PollAnswer]
    :param state: State instance with survey and question data
    :type state: FSMContext
    """
    # TODO get name of the survey from state data
    state_data: Dict[uint32, List[str, str]] = await state.get_data()
    survey_response_id = next(iter(state_data))
    survey_response = SurveyResponse(survey_response_id)
    await survey_response.set_info_db()
    user = survey_response.user
    question_name = state_data[survey_response_id].pop(0)['name']
    question = Question(question_name)
    question_response = Response(question, survey_response, user)

    print(type(response))
    if type(response) == 'aiogram.types.base.MetaTelegramObject':
        answer = str(response)
        print(answer)
        question_response.answer = answer

    await question_response.save()

    await state.set_data(state_data)

    if (state_data[survey_response_id] == []):
        responses_survey_manager.notify(survey_response)
    else:
        send_next_question(response.bot, user.user_id_tel, state_data)
    # Get survey response instance
    # Get Survey instance
    # Get question to a survey id from state data(pop)
    # Save answer in database
    # if list of question id is empty - notify SurveyResponse
    # Get next question to a survey id from state data
    # else send next question using type (another function)


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
