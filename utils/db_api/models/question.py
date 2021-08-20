"""Model to declare classes related with question."""
from numpy import uint32
from typing import List


class Question:
    """Class to declare Daisy Knit question"""

    def __init__(self, id: uint32):
        self.id = id
        self.type: str = None
        self.name: str = None
        self.name_eng: str = None

    async def set_info_db(self):
        """Sets info about question from mysql db to fields
        """
        # TODO fil fields from db
        pass

    async def get_response_choices(self) -> List[str]:
        """Gets response choices from mysql db

        :return: List of responses choices
        :rtype: List[str]
        """
        pass
