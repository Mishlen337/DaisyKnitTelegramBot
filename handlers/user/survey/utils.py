"""Module to send question in Telegram Bot."""

from typing import Dict, List
from numpy import uint32
from aiogram.bot import Bot
from utils.db_api.models.question import Question
from utils.db_api.models.survey_response import SurveyResponse
from keyboards.inline.consts import InlineConstructor as ic
from aiogram.utils.callback_data import CallbackData


async def send_next_question(bot: Bot, user_id_tel: uint32,
                             state_data: Dict[str, List[str]]):
    survey_response_id = next(iter(state_data))
    # Get question name from state data
    question_name = state_data[survey_response_id][0]['name']
    question = Question(question_name)
    await question.set_info_db()

    survey_response = SurveyResponse(survey_response_id)
    await survey_response.set_info_db()
    question_count = len(await survey_response.survey.get_questions())
    question_num = question_count - len(state_data[survey_response_id]) + 1

    question_template = f"[{question_num}/{question_count}] {question_name}"

    if question.type == "quiz":
        responses_choice = await question.get_response_choices()
        list_responses_choice = []
        for choice in responses_choice:
            list_responses_choice.append(choice['name'])

        await bot.send_poll(chat_id=user_id_tel, question=question_template,
                            options=list_responses_choice, type='quiz',
                            correct_option_id=len(list_responses_choice) - 1,
                            is_anonymous=False)

    if question.type == "callback":
        responses_choice = await question.get_response_choices()
        action_list = []
        for response in responses_choice:
            action_list.append((response['name'],
                                response,
                                CallbackData("question", "name")))
        keyboard = ic._create_kb(actions=action_list,
                                 schema=[len(responses_choice)])
        await bot.send_message(user_id_tel, text=question_template,
                               reply_markup=keyboard)

    if question.type == "message":
        await bot.send_message(user_id_tel, text=question_template)
