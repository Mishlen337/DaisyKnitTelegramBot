"""Module to declare users responses to a survey."""

from typing import Dict

from .user import User
from .survey import Survey
from utils.db_api.consts import RawConnection as cn
from numpy import uint32


class SurveyResponse:
    """Class to declare users responses to a survey."""

    def __init__(self, id: uint32):
        self.id = id
        self.survey: Survey = None
        self.user: User = None
        self.is_finished = False

    async def set_info_db(self):
        """Gets info about question from mysql db."""

        sql = """SELECT s.name, u.user_id_tel, sr.is_finished FROM daisyKnitSurvey.survey_response sr
        JOIN daisyKnitSurvey.user u ON sr.user_id = u.id
        JOIN daisyKnitSurvey.survey s ON sr.survey_id = s.id
        WHERE sr.id = %s;"""
        params = (self.id,)
        info = await cn._make_request(sql, params, True)
        if info is None:
            return
        survey_name = info['name']
        self.survey = Survey(survey_name)
        await self.survey.set_info_db()
        user_id_tel = info['user_id_tel']
        self.user = User(user_id_tel)
        await self.user.set_info_db()

        self.is_finished = info['is_finished']

    async def get_responses_db(self) -> Dict[str, str]:
        """Gets respones to this survey from mysql db

        :return: responses to this survey
        :rtype: Dict[str, str]
        """
        # TODO get responses from db
        sql = """SELECT q.name, r.answer FROM daisyKnitSurvey.response r
        JOIN daisyKnitSurvey.question q ON r.question_id = q.id
        JOIN daisyKnitSurvey.user u ON u.id = r.user_id
        WHERE r.user_id = %s AND r.survey_response_id = %s;
        """
        params = (self.user.id, self.id)
        info = await cn._make_request(sql, params, True, True)
        return info

    @staticmethod
    async def save(survey: Survey, user: User):
        """Saves new survey response in mysql db and returns its instance

        :param survey: Survey instance
        :type survey: Survey
        :param user: User instance
        :type user: User
        :return: SurveyResponse instance
        :rtype: SurveyResponse
        """
        sql = """INSERT daisyKnitSurvey.survey_response (survey_id, user_id, is_finished)
        VALUES (%s, %s, %s);"""
        params = (survey.id, user.id, False)
        await cn._make_request(sql, params)
        sql = """SELECT LAST_INSERT_ID() as id
        FROM daisyKnitSurvey.survey_response;"""
        info = await cn._make_request(sql, fetch=True)
        assert not (info is None), "Invalid insertion"
        id = info['id']
        survey_response = SurveyResponse(id)
        survey_response.survey = survey
        survey_response.user = user
        survey_response.is_finished = False
        return survey_response

    async def finish(self):
        sql = """UPDATE daisyKnitSurvey.survey_response SET is_finished = %s WHERE id = %s;"""
        params = (True, self.id)
        await cn._make_request(sql, params)
