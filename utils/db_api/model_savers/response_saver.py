"""Module to declare saver to put response model in mysql db."""

from contracts import contract
from utils.db_api.model_savers.abstract_saver import AbstractSaver
from utils.db_api.models.response import Response
from utils.db_api.consts import RawConnection


class ResponseSaver(AbstractSaver):
    """Class to declare saver to put response model in mysql db."""

    @contract
    @staticmethod
    async def save(model: Response):
        """Saves response in mysql db

        :param model: users response to a surveys question
        :type model: Response
        """
        # TODO save response info in mysql db
        # info user_id, question_id, survey_response
        pass
