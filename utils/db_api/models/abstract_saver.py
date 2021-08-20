"""Module to declare abstract saver to put model in mysql db."""

from abc import ABC, abstractstaticmethod


class AbstractSaver(ABC):
    """Class to declare abstract saver to put model in mysql db."""

    @staticmethod
    @abstractstaticmethod
    async def save(model):
        """Saves model in mysql db

        :param model: mysql db model
        """
        pass
