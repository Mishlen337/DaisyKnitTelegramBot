"""Module to declare users response."""

from contracts import contract
from utils.db_api.models.survey import Question
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.user import User


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
    async def get_response_db() -> str:
        """Gets string response from mysql db and set value to answer

        :return: string response
        :rtype: str
        """
        # TODO Save response to self.answer
        # Return self.answer
        pass
