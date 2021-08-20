"""Module to declare users responses to a survey."""

from utils.db_api.models.response import Response
from contracts import contract
from typing import Dict, List
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from utils.db_api.models.abstract_saver import AbstractSaver


class SurveyResponse:
    """Class to declare users responses to a survey."""

    def __init__(self, id: str):
        self.id = id
        self.survey: Survey = None
        self.user: User = None

    @contract
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


class SurveyResponseSaver(AbstractSaver):
    """Class to declare saver to put survey response model in mysql db."""

    @staticmethod
    @contract
    async def save(model: List[Survey, Response]) -> SurveyResponse:
        """Saves new survey response in mysql db and returns id

        :param model: List of sur
        :type model: List[Survey, Response]
        :return: SurveyResponse instance
        :rtype: SurveyResponse
        """
        # TODO put info in survey response table
        # info: survey_id, user_id
        pass
