"""Module to declare users responses to a survey."""

from contracts import contract
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from typing import Dict


class SurveyResponse:
    """Class to declare users responses to a survey."""

    async def __init__(self, id: str):
        self.id = id
        self.survey: Survey = None
        self.user: User = None
        await self._set_survey_response_info_db(id)

    @contract
    async def _set_survey_response_info_db(self, id: str):
        """Gets info about question from mysql db

        :param id: survey_response in mysql db
        :type id: str
        """
        # TODO fil fields from db
        pass

    @contract
    async def get_responses_db(self, user: User) -> Dict[str, str]:
        """Gets respones to this survey from mysql db

        :param user: user instance
        :type user: User
        :return: responses to this survey
        :rtype: Dict[str, str]
        """
        # TODO get responses from db
