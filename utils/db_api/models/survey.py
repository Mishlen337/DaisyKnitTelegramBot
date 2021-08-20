"""Model to declare classes related with survey."""

from typing import List
from datetime import datetime
from numpy import uint32


class Survey:
    """Class to declare Daisy Knit survey."""
    def __init__(self, name: str):
        self.name = name
        self.id: uint32 = None
        self.description: str = None
        # Time, when survey was updated
        self.updated_at: datetime = None

    async def set_info_db(self):
        """Gets info about question from mysql db
        """
        # TODO fil fields from db
        pass

    async def get_questions(self) -> List[uint32]:
        """Gets questions of a survey from mysql db

        :return: List of quiestions id
        :rtype: List[uint32]
        """
        pass
