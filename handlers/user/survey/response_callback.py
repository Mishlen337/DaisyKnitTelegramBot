"""Modules to declare handlers for surveys callback response."""

from typing import Dict, Union, List
from contracts import contract
from aiogram.types import CallbackQuery, Message, PollAnswer
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from numpy import uint32
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.question import Question
from utils.db_api.models.response import Response
from .utils import send_next_question
from notifiers.survey_response.manager import ResponsesSurveyManager
from notifiers.survey_response.subscribers import \
    MindBoxResponsesSurveyNotifier, LoggerResponsesSurveyNotifier


class ResponseCallback:
    """Class to declare handler of callback response."""

    def __init__(self):
        _rs_subscribers = [LoggerResponsesSurveyNotifier(),
                           MindBoxResponsesSurveyNotifier()]
        self.responses_survey_manager = ResponsesSurveyManager()
        for sub in _rs_subscribers:
            self.responses_survey_manager.subscribe(sub)

    async def get_response(self, response: CallbackQuery,
                           state: FSMContext):
        """Response handler to get response

        :param response: Response to a question instance
        :type response: CallbackQuery
        :param state: State instance with survey and question data
        :type state: FSMContext
        """
        user_id_tel = response.from_user.id
        state_data: Dict[uint32, List[str, str]] = await state.get_data()

        survey_response_id = next(iter(state_data))
        survey_response = SurveyResponse(survey_response_id)
        await survey_response.set_info_db()
        user = survey_response.user
        question_name = state_data[survey_response_id].pop(0)['name']
        question = Question(question_name)
        await question.set_info_db()

        question_response = Response(question, survey_response, user)
        question_response.answer = response.data.split(':')[-1]
        await question_response.save()

        await state.set_data(data=state_data)

        edited_text = response.message.text + "\n" + f"""Ваш ответ:
        {question_response.answer}"""
        await response.bot.edit_message_text(text=edited_text,
                                             chat_id=response.from_user.id,
                                             message_id=response.message.message_id,
                                             reply_markup=InlineKeyboardMarkup())

        if (state_data[survey_response_id] == []):
            await self.responses_survey_manager.notify(survey_response)
            await response.bot.send_message(user_id_tel,
                                            text="Спасибо за опрос:)")
            await state.set_state(state="initial_state")
            await state.reset_data(user=user_id_tel)
        else:
            await send_next_question(response.bot, user.user_id_tel,
                                     state_data)

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
