"""Module to declare managers subscribers."""

from contracts import contract
from notifiers.abstracts import AbstractSurveyObserver


class TelegramBotSurveyNotifier(AbstractSurveyObserver):
    """Notifier to send invitation survey in Telegram bot."""

    def __init__(self):
        # TODO initialize variables to send invitation
        # variable to send information to telgram API
        # template message of invitation
        # template message of keyboard
        pass

    @contract
    async def update(self, event_args):
        """Sends invitation survey in Telegram bot to take a survey.

        :param event_args: data of a survey event
        :type event_args: [type]
        """
        # TODO Send invitation in Telegram bot
        pass


class LoggerSurveyNotifier(AbstractSurveyObserver):
    """Notifier to log info about invitation survey."""

    def __init__(self):
        # TODO initialize variables to log invitation
        # variable to log information in file
        # template string of invitation
        pass

    @contract
    async def update(self, event_args):
        """Logs info about invitation survey in file.

        :param event_args: data of a survey event
        :type event_args: [type]
        """
        # TODO Log info in file
        pass
