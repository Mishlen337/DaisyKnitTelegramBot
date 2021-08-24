"""Module to handle response to a quiz question."""

from typing import Dict, List
from aiogram.types import PollAnswer
from aiogram.dispatcher import Dispatcher
from contracts import contract
from numpy import uint32
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.question import Question
from utils.db_api.models.response import Response
from .utils import send_next_question
from notifiers.survey_response.manager import ResponsesSurveyManager
from notifiers.survey_response.subscribers import \
    MindBoxResponsesSurveyNotifier, LoggerResponsesSurveyNotifier


class QuizResponse:
    """Class to declare handler of quiz response."""
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        _rs_subscribers = [LoggerResponsesSurveyNotifier(),
                           MindBoxResponsesSurveyNotifier()]
        self.responses_survey_manager = ResponsesSurveyManager()
        for sub in _rs_subscribers:
            self.responses_survey_manager.subscribe(sub)

    async def get_response(self, response: PollAnswer):
        """Response handler to get response

        :param response: Response to a question instance
        :type response: Union[CallbackQuery, Message, PollAnswer]
        :param state: State instance with survey and question data
        :type state: FSMContext
        """
        user_id_tel = response.user.id
        state_data: Dict[uint32, List[str, str]] = \
            await self.dp.storage.get_data(user=user_id_tel)

        survey_response_id = next(iter(state_data))
        survey_response = SurveyResponse(survey_response_id)
        await survey_response.set_info_db()
        user = survey_response.user
        question_name = state_data[survey_response_id].pop(0)['name']
        question = Question(question_name)
        await question.set_info_db()

        question_response = Response(question, survey_response, user)

        response_choices = await question.get_response_choices()
        answer = response_choices[response.option_ids[0]]['name']
        question_response.answer = answer

        await question_response.save()

        await self.dp.storage.set_data(user=response.user.id,
                                       data=state_data)

        if (state_data[survey_response_id] == []):
            await self.responses_survey_manager.notify(survey_response)
            await response.bot.send_message(user_id_tel,
                                            text="Спасибо за опрос:)")
            await self.dp.storage.set_state(state="initial_state",
                                            user=user_id_tel)
            await self.dp.storage.reset_data(user=user_id_tel)
        else:
            await send_next_question(response.bot, user.user_id_tel,
                                     state_data)
