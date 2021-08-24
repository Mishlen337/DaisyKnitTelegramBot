"""Module to declare users responses to a survey."""

from typing import Dict
from contracts import contract
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

    async def set_info_db(self):
        """Gets info about question from mysql db."""

        sql = """SELECT sr.survey_id, u.user_id_tel FROM daisyKnitSurvey.survey_response sr
        JOIN daisyKnitSurvey.User u ON sr.user_id = u.id
        WHERE sr.id = %s;"""
        params = (self.id,)
        info = await cn._make_request(sql, params)
        print(info)
        survey_id = info[0]
        self.survey = Survey(survey_id)
        user_id_tel = info[1]
        self.user = User(user_id_tel)

    async def get_responses_db(self) -> Dict[str, str]:
        """Gets respones to this survey from mysql db

        :return: responses to this survey
        :rtype: Dict[str, str]
        """
        # TODO get responses from db
        sql = """SELECT q.name_eng, r.answer FROM daisyKnitSurvey.response r
        JOIN daisyKnitSurvey.question q ON r.question_id = q.id
        WHERE r.user_id = %s AND r.survey_response_id = %s;
        """
        params = (self.user.id, self.id)
        info = await cn._make_request(sql, params, True, True)
        # TODO make Dict
        return info

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
        sql = """INSERT daisyKnitSurvey.survey_response (survey_id, user_id)
        VALUES (%s, %s);"""
        params = (survey.id, user.id)
        await cn._make_request(sql, params)
        sql = """SELECT LAST_INSERT_ID() as id
        FROM daisyKnitSurvey.survey_response;"""
        info = await cn._make_request(sql, fetch=True)
        assert not (info is None), "Invalid insertion"
        id = info['id']
        survey_response = SurveyResponse(id)
        survey_response.survey = survey
        survey_response.user = user
        return survey_response
