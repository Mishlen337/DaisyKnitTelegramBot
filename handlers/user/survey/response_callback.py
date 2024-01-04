"""Modules to declare handlers for surveys callback response."""

from numpy import uint32
from loguru import logger
from typing import Dict, List

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from .utils import send_next_question
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.question import Question
from utils.db_api.models.response import Response

from notifiers.survey_response.manager import ResponsesSurveyManager
from notifiers.survey_response.subscribers import ResponsesSurveyManagersNotifier, LoggerResponsesSurveyNotifier


class ResponseCallback:
    """Class to declare handler of callback response."""

    def __init__(self, dp: Dispatcher):
        _rs_subscribers = [LoggerResponsesSurveyNotifier(),
                           ResponsesSurveyManagersNotifier(dp)]
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
        try:
            user_id_tel = response.from_user.id
            survey: Dict[uint32, List[str, str]] = (await state.get_data())["survey"]

            survey_response_id = next(iter(survey))
            survey_response = SurveyResponse(survey_response_id)
            await survey_response.set_info_db()
            user = survey_response.user
            question_name = survey[survey_response_id].pop(0)['name']
            question = Question(question_name)
            await question.set_info_db()

            question_response = Response(question, survey_response, user)
            question_response.answer = response.data.split(':')[-1]
            await question_response.save()


            edited_text = response.message.text + "\n" + f"""Ваш ответ:
            {question_response.answer}"""
            await response.bot.edit_message_text(text=edited_text,
                                                chat_id=response.from_user.id,
                                                message_id=response.message.message_id,
                                                reply_markup=InlineKeyboardMarkup())

            if (survey[survey_response_id] == []):
                await survey_response.finish()
                await response.bot.send_message(user_id_tel, text=f"Заказ/опрос № {survey_response_id}\nУзнать как и где забрать заказ, напишите /help\nОформить новый заказ, напишите /start")
                await state.set_state(state="initial_state")
                await state.reset_data()
                await self.responses_survey_manager.notify(survey_response)
            else:
                sent_message = await send_next_question(response.bot, user.user_id_tel, survey)
                await state.set_data({"survey": survey, "last_question_message_id": sent_message.message_id})

        except Exception as ex:
            logger.error(ex)
            await response.bot.send_message(response.from_user.id, "Проблемы с базой данных. Попробуйте позже! Поддержка @mishlen25")

    async def get_response_error(self, response: CallbackQuery, state: FSMContext):
        """Response handler to send message about finishing
        previous survey

        :param response: Response to a question instance
        :type response: Union[CallbackQuery, Message, PollAnswer]
        :param state: State instance with survey and question data
        :type state: FSMContext
        """
        await response.answer("У вас есть активный заказ/опрос\nПройдите его. Для того, чтобы его закончить преждевременно, напишите /finish", show_alert=True)


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
