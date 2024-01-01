"""Module to declare managers subscribers."""
from typing import List
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.types import InputFile
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
        excel_filename = f"results_{event_args.user.user_id_tel}.xlsx"
        # pd.DataFrame(responses).to_excel(excel_filename)
        ##########
        writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')
        pd.DataFrame(responses).to_excel(writer, sheet_name='Sheet1', index=False)

        #modifyng output by style - wrap
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']
        wrap_format = workbook.add_format({'text_wrap': True})
        writer.close()
        ############
        for mtid in self.manager_tel_ids:
            f = InputFile(excel_filename, "results.xlsx")
            await self.dp.bot.send_document(chat_id=mtid, document=f, caption=f'Новый заказ/опрос от @{event_args.user.username}')
