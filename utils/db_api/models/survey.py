"""Model to declare classes related with survey."""

from contracts import contract
from typing import List
from datetime import datetime
from question import Question


class Survey:
    """Class to declare Daisy Knit survey"""
    async def __init__(self, name: str):
        self.name = name
        self.id: str = None
        self.description: str = None
        # Time, when survey was updated
        self.updated_at: datetime = None
        self.questions: List[Question] = []
        await self._set_survey_info_db(name)

    @contract
    async def _set_survey_info_db(self, name: str):
        """Gets info about question from mysql db

        :param name: survey name in db
        :type name: str
        """
        # TODO fil fields from db
        pass
