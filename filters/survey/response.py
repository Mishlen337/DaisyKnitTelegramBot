"""Module to declare filters for surveys questions."""

from typing import Dict, Union
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery, PollAnswer, Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.dispatcher import Dispatcher
from contracts import contract
from utils.db_api.models.question import Question


class ResponseValidFilter(BoundFilter):
    """Filter to check whether response is valid or not."""

    key = "response_is_valid"

    def __init__(self, response_is_valid, dp: Dispatcher):
        self.dp = dp
        self.response_is_valid = response_is_valid
        self.question_types = {"callback": CallbackQuery, "quiz": PollAnswer,
                               "message": Message}

    async def check(self, response: Union[CallbackQuery, PollAnswer, Message]):
        """Checks whether response is valid or not.

        :param question: Response associated with a question
        :type question: Union[CallbackQuery, PollAnswer, Message]
        """
        state = {}
        if isinstance(response, PollAnswer):
            state = await self.dp.storage.get_data(user=response.user.id)
        else:
            state = await self.dp.storage.get_data(user=response.from_user.id)
        try:
            survey_response_id = next(iter(state))
        except StopIteration:
            return False
        # Get question name from state data
        question_name = state[survey_response_id][0]['name']
        question = Question(question_name)
        await question.set_info_db()
        return self.response_is_valid == isinstance(response,
                                                    self.question_types[question.type])
