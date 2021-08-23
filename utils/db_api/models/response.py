"""Module to declare users response."""

from utils.db_api.models.question import Question
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

    async def set_info_db():
        """Sets string response from mysql db

        """
        # TODO Save response to self.answer
        # Return self.answer
        pass

    async def save(self):
        """Saves response in mysql db

        """
        # TODO save response info in mysql db
        # info user_id, question_id, survey_response
        pass
