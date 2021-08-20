"""Module to declare managers subscribers."""

import asyncio
from notifiers.abstracts import AbstractSurveyObserver
from .event_args import SurveyEventArgs


class TelegramBotSurveyNotifier(AbstractSurveyObserver):
    """Notifier to send invitation survey in Telegram bot."""

    def __init__(self):
        # TODO initialize variables to send invitation
        # variable to send information to telgram API
        # template message of invitation
        # template message of keyboard
        pass

    async def update(self, event_args: SurveyEventArgs):
        """Sends invitation survey in Telegram bot to take a survey.

        :param event_args: data of a survey event
        :type event_args: SurveyEventArgs
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

    async def update(self, event_args: SurveyEventArgs):
        """Logs info about invitation survey in file.

        :param event_args: data of a survey event
        :type event_args: SurveyEventArgs
        """
        print(event_args.user.user_id_tel)
        print(event_args.survey.name)
        await asyncio.sleep(1.0)
        # TODO Log info in file
