"""Model to declare classes related with question."""

from contracts import contract
from typing import List
from utils.db_api.models.response import Response
from utils.db_api.models.user import User
from utils.db_api.models.survey_response import SurveyResponse


class Question:
    """Class to declare Daisy Knit question"""

    async def __init__(self, id: str):
        self.id: str = id
        self.type: str = None
        self.response_choices: List[Response] = None
        self.name: str = None
        self.name_eng: str = None
        await self._set_question_info_db(id)

    @contract
    async def _set_question_info_db(self, id: str):
        """Gets info about question from mysql db

        :param id: question id in db
        :type id: str
        """
        # TODO fil fields from db
        pass

    @contract
    async def get_response_db(self, survey_response: SurveyResponse,
                              user: User) -> List[Response]:
        """Gets response to a question

        :param survey_response: survey response that contains answer
        :type survey_response: Surveys response
        :param user: user, that answers this question
        :type user: User
        :return: users response
        :rtype: List[Response]
        """
        # TODO get response
        pass
