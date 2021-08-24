"""Module to send question in Telegram Bot."""
from typing import Dict, List
from numpy import uint32
from aiogram.bot import Bot
from utils.db_api.models.question import Question


async def send_next_question(bot: Bot, user_id: uint32,
                             state_data: Dict[str, List[str]]):
    survey_response_id = next(iter(state_data))
    # Get question name from state data
    question_name = state_data[survey_response_id][0]['name']
    print(question_name)
    question = Question(question_name)
    await question.set_info_db()
    if question.type == "quiz":
        responses_choice = await question.get_response_choices()
        list_responses_choice = []
        for choice in responses_choice:
            list_responses_choice.append(choice['name'])
        await bot.send_poll(chat_id=user_id, question=question_name,
                            options=list_responses_choice, type='quiz',
                            correct_option_id=len(list_responses_choice) - 1,
                            is_anonymous=False)
