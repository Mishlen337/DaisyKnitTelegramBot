"""Module to declare saver to put survey response model in mysql db."""

from contracts import contract
from utils.db_api.model_savers.abstract_saver import AbstractSaver
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.consts import RawConnection


class SurveyResponseSaver(AbstractSaver):
    """Class to declare saver to put survey response model in mysql db."""

    @contract
    @staticmethod
    async def save(model: SurveyResponse):
        """Saves survey response in mysql db

        :param model: response to a survey
        :type model: SurveyResponse
        """
        # TODO put info in survey response table
        # info: survey_id, user_id
        pass
