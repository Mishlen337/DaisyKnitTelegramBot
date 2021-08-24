"""Module to handle response to a quiz question."""

from typing import Dict, Union, List
from aiogram import types
from aiogram.types import CallbackQuery, Message, PollAnswer, Poll
from aiogram.dispatcher import FSMContext, Dispatcher
from contracts import contract
from numpy import uint32
from utils.db_api.models.survey_response import SurveyResponse
from utils.db_api.models.question import Question
from utils.db_api.models.response import Response
from data.events import responses_survey_manager
from .utils import send_next_question


class QuizResponse:
    def __init__(self, dp: Dispatcher):
        self.dp = dp

    async def get_response(self, response: PollAnswer):
        """Response handler to get response

        :param response: Response to a question instance
        :type response: Union[CallbackQuery, Message, PollAnswer]
        :param state: State instance with survey and question data
        :type state: FSMContext
        """
        # TODO get name of the survey from state data
        # state_data = response.conf
        user_id_tel = response.user.id
        state_data: Dict[uint32, List[str, str]] = \
            await self.dp.storage.get_data(user=user_id_tel)
        print("state_date", state_data)
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
        print("answer", answer)
        question_response.answer = answer

        await question_response.save()

        await self.dp.storage.set_data(user=response.user.id,
                                       data=state_data)

        if (state_data[survey_response_id] == []):
            await responses_survey_manager.notify(survey_response)
        else:
            await send_next_question(response.bot, user.user_id_tel, state_data)
        # Get survey response instance
        # Get Survey instance
        # Get question to a survey id from state data(pop)
        # Save answer in database
        # if list of question id is empty - notify SurveyResponse
        # Get next question to a survey id from state data
        # else send next question using type (another function)


async def get_response_error(response: Union[CallbackQuery,
                                            Message,
                                            PollAnswer],
                             state: FSMContext):
    """Response handler to send message about finishing
    previous survey

    :param response: Response to a question instance
    :type response: Union[CallbackQuery, Message, PollAnswer]
    :param state: State instance with survey and question data
    :type state: FSMContext
    """
    # TODO send message to finish previous survey
    pass
