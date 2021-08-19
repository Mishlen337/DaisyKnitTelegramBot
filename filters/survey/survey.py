"""Module to declare filters for a survey."""

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from contracts import contract


class SurveyActiveFilter(BoundFilter):
    """Filter to check whether survey is active or not"""

    key = "survey_is_active"

    @contract
    def check(self, call: types.CallbackQuery) -> bool:
        """Checks whether survey is active or not

        :param call: Callback instance caused by the inline button
        :type call: types.CallbackQuery
        :return: whether survey is active or not
        :rtype: bool
        """
        # TODO get survey id by callback name using mysql db
        # get user poll list in Redis by survey id
        # None - False else True
        return False


class SurveyValidFilter(BoundFilter):
    """Filter to check whether survey name is valid or not."""

    key = "survey_is_valid"

    @contract
    def check(self, call: types.CallbackQuery) -> bool:
        """Checks whether survey is valid or not

        :param call: Callback instance caused by the inline button
        :type call: types.CallbackQuery
        :return: whether survey is valid or not
        :rtype: bool
        """
        # TODO get survey id by callback name using mysql db
        # if id = None - False else true
        return False
