"""Module to declare filters for surveys questions."""

from typing import Dict, Union
from loguru import logger
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery, PollAnswer, Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.dispatcher import Dispatcher

from utils.db_api.models.question import Question


class ResponseTypeValidFilter(BoundFilter):
    """Filter to check whether response is valid or not."""

    key = "response_is_valid"

    def __init__(self, response_is_valid, dp: Dispatcher):
        self.dp = dp
        self.response_is_valid = response_is_valid
        self.question_types = {"callback": CallbackQuery,
                               "schedule": CallbackQuery,
                               "quiz": PollAnswer,
                               "message": Message}

    async def check(self, response: Union[CallbackQuery, PollAnswer, Message]):
        """Checks whether response is valid or not.

        :param question: Response associated with a question
        :type question: Union[CallbackQuery, PollAnswer, Message]
        """
        try:
            survey = {}
            if isinstance(response, PollAnswer):
                survey = (await self.dp.storage.get_data(user=response.user.id))["survey"]
            else:
                survey = (await self.dp.storage.get_data(user=response.from_user.id))["survey"]
            try:
                survey_response_id = next(iter(survey))
            except StopIteration:
                return False
            # Get question name from state data
            question_name = survey[survey_response_id][0]['name']
            question = Question(question_name)
            await question.set_info_db()
            return self.response_is_valid == isinstance(response,
                                                        self.question_types[question.type])
        except Exception as ex:
            logger.error(ex)
            await response.bot.send_message(response.from_user.id, "Проблемы с базой данных. Попробуйте позже! Поддержка @mishlen25")
            return False

class ResponseCallbackValidFilter(BoundFilter):
    """Filter to check whether response is valid or not."""

    key = "response_is_valid"

    def __init__(self, response_is_valid, dp: Dispatcher):
        self.dp = dp
        self.response_is_valid = response_is_valid

    async def check(self, response: CallbackQuery):
        """Checks whether response is valid or not.

        :param question: Response associated with a question
        :type question: CallbackQuery
        """
        try:
            last_question_message_id = (await self.dp.storage.get_data(user=response.from_user.id))["last_question_message_id"]
            return self.response_is_valid == (last_question_message_id == response.message.message_id)

        except Exception as ex:
            logger.error(ex)
            await response.bot.send_message(response.from_user.id, "Проблемы с базой данных. Попробуйте позже! Поддержка @mishlen25")
            return False
