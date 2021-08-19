"""Module to declare managers subscribers."""

from contracts import contract
from notifiers.abstracts import AbstractResponsesSurveyObserver


class MindBoxResponsesSurveyNotifier(AbstractResponsesSurveyObserver):
    """Notifier to send responses to a survey to MindBox API."""

    def __init__(self):
        # TODO initialize variables to send responses
        # template for query
        pass

    @contract
    async def update(self, event_args):
        """Sends responses to a survey to MindBox API

        :param event_args: data of responses to a survey event
        :type event_args: [type]
        """
        # TODO send data to MindBox if user is authorized
        pass


class LoggerResponsesSurveyNotifier(AbstractResponsesSurveyObserver):
    """Notifier to log info about responses in file."""

    def __init__(self):
        # TODO initialize variables to log info in file
        # variable to log information in file
        # template string of info
        pass

    async def update(self, event_args):
        """Logs info about responses in fil

        :param event_args: data of responses to a survey event
        :type event_args: [type]
        """
        # TODO Log info in file
        pass
