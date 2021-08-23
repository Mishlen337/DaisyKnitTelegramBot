"""Module to declare users response."""

from .question import Question
from .survey_response import SurveyResponse
from .user import User
from utils.db_api.consts import RawConnection as cn


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

    async def set_info_db(self):
        """Sets string response from mysql db."""

        sql = """SELECT answer FROM daisyKnitSurvey.response
        WHERE user_id = %s AND question_id = %s
        AND survey_response_id = %s;"""
        params = (self.user.id, self.question, self.survey_response.id)
        answer = await cn._make_request(sql, params, True)
        self.answer = answer

    async def save(self):
        """Saves response in mysql db."""
        sql = """INSERT daisyKnitSurvey.response
        (user_id, question_id, survey_response_id, answer)
        VALUE (%s, %s, %s, %s);"""
        params = (self.user.id, self.question.id, self.survey_response.id,
                  self.answer)
        await cn._make_request(sql, params)
