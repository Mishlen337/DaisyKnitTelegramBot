"""Module to declare users response."""

from contracts import contract
from utils.db_api.models.survey import Question
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.user import User
from utils.db_api.models.abstract_saver import AbstractSaver


class Response:
    """Class to declare response of question to a survey from user."""

    def __init__(self,
                 question: Question,
                 survey_response: SurveyResponse,
                 user: User,
                 answer: str = None):
        self.user = user
        self.question = question
        self.survey_response = survey_response
        self.answer = answer

    @contract
    async def set_info_db():
        """Sets string response from mysql db

        """
        # TODO Save response to self.answer
        # Return self.answer
        pass


class ResponseSaver(AbstractSaver):
    """Class to declare saver to put response model in mysql db."""

    @contract
    @staticmethod
    async def save(model: Response):
        """Saves response in mysql db

        :param model: users response to a surveys question
        :type model: Response
        """
        # TODO save response info in mysql db
        # info user_id, question_id, survey_response
        pass
