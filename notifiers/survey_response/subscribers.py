"""Module to declare managers subscribers."""
from typing import List
from aiogram.dispatcher.dispatcher import Dispatcher
import pandas as pd
# pd.set_option('display.max_columns', None)

from data import config
from notifiers.abstracts import AbstractResponsesSurveyObserver
from utils.db_api.models.survey_response import SurveyResponse


class MindBoxResponsesSurveyNotifier(AbstractResponsesSurveyObserver):
    """Notifier to send responses to a survey to MindBox API."""

    def __init__(self):
        # TODO initialize variables to send responses
        # template for query
        pass

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

    async def update(self, event_args: SurveyResponse):
        """Logs info about responses in fil

        :param event_args: data of responses to a survey event
        :type event_args: [type]
        """
        # TODO Log info in file
        print(await event_args.get_responses_db())


class ResponsesSurveyManagersNotifier(AbstractResponsesSurveyObserver):
    def __init__(self, dp: Dispatcher) -> None:
        self.manager_tel_ids = config.MANAGER_TEL_IDS
        self.dp = dp

    async def update(self, event_args: SurveyResponse):
        """Logs info about responses in fil

        :param event_args: data of responses to a survey event
        :type event_args: [type]
        """
        responses = await event_args.get_responses_db()
        markdown_responses = pd.DataFrame(responses).T.to_markdown()
        for mtid in self.manager_tel_ids:
            await self.dp.bot.send_message(chat_id=mtid, text='Новый заказ/опрос!')
            await self.dp.bot.send_message(chat_id=mtid, text='<code>' + markdown_responses + '</code>', parse_mode="HTML")
