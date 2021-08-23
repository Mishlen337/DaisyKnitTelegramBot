"""Module to declare users responses to a survey."""

from typing import Dict
from contracts import contract
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey


class SurveyResponse:
    """Class to declare users responses to a survey."""

    def __init__(self, id: str):
        self.id = id
        self.survey: Survey = None
        self.user: User = None

    async def set_info_db(self):
        """Gets info about question from mysql db

        """
        # TODO fil fields from db
        pass

    async def get_responses_db(self) -> Dict[str, str]:
        """Gets respones to this survey from mysql db

        :return: responses to this survey
        :rtype: Dict[str, str]
        """
        # TODO get responses from db

    @staticmethod
    @contract
    async def save(survey: Survey, user: User):
        """Saves new survey response in mysql db and returns its instance

        :param survey: Survey instance
        :type survey: Survey
        :param user: User instance
        :type user: User
        :return: SurveyResponse instance
        :rtype: SurveyResponse
        """
        # TODO put info in survey response table
        # info: survey_id, user_id
        # get id of insertion
        # get survey response instance
        pass
