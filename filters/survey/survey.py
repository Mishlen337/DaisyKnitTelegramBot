"""Module to declare filters for a survey."""

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from contracts import contract
from utils.db_api.models.survey import Survey


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

    key = "is_survey"

    def __init__(self, is_survey: bool):
        self.is_survey = is_survey

    async def check(self, call: types.CallbackQuery) -> bool:
        """Checks whether survey should be started or not

        :param call: Callback instance caused by the inline button
        :type call: types.CallbackQuery
        :return: whether survey should be started or not
        :rtype: bool
        """
        survey = Survey(call.data)
        await survey.set_info_db()
        return not (survey.id is None) == self.is_survey
