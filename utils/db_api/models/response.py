"""Module to declare users response."""
from datetime import datetime
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
        self.created = None

    async def set_info_db(self):
        """Sets string response from mysql db."""

        sql = """SELECT answer FROM daisyKnitSurvey.response
        WHERE user_id = %s AND question_id = %s
        AND survey_response_id = %s;"""
        params = (self.user.id, self.question, self.survey_response.id)
        info = await cn._make_request(sql, params, True)
        if info is None:
            return
        self.answer = info['answer']

    async def is_unique(self):
        sql = """SELECT answer FROM daisyKnitSurvey.response
        WHERE question_id = %s
        AND answer = %s;"""
        params = (self.question.id, self.answer)
        res = await cn._make_request(sql, params, True)
        return res is None

    async def save(self):
        """Saves response in mysql db."""
        sql = """INSERT daisyKnitSurvey.response
        (user_id, question_id, survey_response_id, answer, created)
        VALUE (%s, %s, %s, %s, %s);"""
        self.created = datetime.now()
        params = (self.user.id, self.question.id, self.survey_response.id,
                  self.answer, self.created)
        await cn._make_request(sql, params)
