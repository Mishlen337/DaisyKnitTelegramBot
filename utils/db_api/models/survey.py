"""Model to declare classes related with survey."""

from typing import List, Dict
from datetime import datetime
from numpy import uint32
from utils.db_api.consts import RawConnection as cn


class Survey:
    """Class to declare Daisy Knit survey."""
    def __init__(self, name: str):
        self.name = name
        self.id: uint32 = None
        self.description: str = None
        # Time, when survey was updated
        self.updated: datetime = None

    async def set_info_db(self):
        """Gets info about question from mysql db."""

        sql = """
        SELECT id, description, updated FROM daisyKnitSurvey.survey
        WHERE name = %s;
        """
        params = (self.name,)
        info = await cn._make_request(sql, params, True)
        if info is None:
            return
        self.id = info['id']
        self.description = info['description']
        self.updated = info['updated']

    async def get_questions(self) -> List[Dict[str, str]]:
        """Gets questions of a survey from mysql db

        :return: Sorted list of quiestion names
        :rtype: List[Dict[str, str]]
        """
        sql = """SELECT q.name FROM daisyKnitSurvey.question_order qo
        JOIN daisyKnitSurvey.question q ON qo.question_id = q.id
        WHERE qo.survey_id = %s
        ORDER BY qo.order;"""
        params = (self.id,)
        info = await cn._make_request(sql, params, True, True)
        assert not (info is None), "Surveys questions is empty"
        return info

    async def save(self):
        """Saves new info about survey in mysql db."""
        pass
