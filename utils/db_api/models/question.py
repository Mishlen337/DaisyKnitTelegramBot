"""Model to declare classes related with question."""
from numpy import uint32
from typing import List, Dict
from contracts import contract
from utils.db_api.consts import RawConnection as cn


class Question:
    """Class to declare Daisy Knit question"""

    def __init__(self, name: str):
        self.name = name
        self.id: uint32 = None
        self.name_eng: str = None
        self.type: str = None

    async def set_info_db(self):
        """Sets info about question from mysql db to fields."""
        sql = """SELECT q.id, q.name_eng, qt.name FROM daisyKnitSurvey.question q
        JOIN daisyKnitSurvey.question_type qt
        ON q.question_type_id = qt.id
        WHERE q.name = %s;"""
        params = (self.name,)
        info = await cn._make_request(sql, params, True)
        if info is None:
            return
        self.id = info['id']
        self.name_eng = info['name_eng']
        self.type = info['name']

    async def get_response_choices(self) -> List[Dict[str, str]]:
        """Gets response choices from mysql db

        :return: List of responses choices
        :rtype: List[str]
        """
        sql = """SELECT rc.name FROM daisyKnitSurvey.response_choice_order rco
        JOIN daisyKnitSurvey.response_choice rc
        ON rco.response_choice_id = rc.id
        WHERE rco.question_id = %s;"""
        params = (self.id,)
        info = await cn._make_request(sql, params, True, True)
        assert not (info is None), "Responses choices of questions is empty"
        return info

    async def save(self):
        """Saves question info in mysql db."""
        # TODO save question info
