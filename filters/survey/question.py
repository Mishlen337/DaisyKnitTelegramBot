"""Module to declare filters for surveys questions."""

from typing import Union
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery, PollAnswer, Message
from contracts import contract


class QuestionValidFilter(BoundFilter):
    """Filter to check whether question is valid or not."""

    key = "question_is_valid"

    @contract
    def check(self,
              question: Union[CallbackQuery, PollAnswer, Message]) -> bool:
        """Checks whether question is valid or not.

        :param question: Response associated with a question
        :type question: Union[CallbackQuery, PollAnswer, Message]
        :return: whether question is valid or not
        :rtype: bool
        """
        # TODO determine the type of the question
        # Get name of the survey and name of the question in mysql
        # Check whether first question in Redis ({user_id}_{survey_id}) =
        # survey and name of the question in mysql
        return False
