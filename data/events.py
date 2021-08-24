"""Module to declare events instances."""

from notifiers.survey.manager import SurveyManager
from notifiers.survey.subscribers import LoggerSurveyNotifier,\
    TelegramBotSurveyNotifier
from notifiers.survey_response.manager import ResponsesSurveyManager
from notifiers.survey_response.subscribers import \
    MindBoxResponsesSurveyNotifier, LoggerResponsesSurveyNotifier

# Survey event declaration 
_subscribers = [LoggerSurveyNotifier(), TelegramBotSurveyNotifier()]
survey_manager = SurveyManager()
for sub in _subscribers:
    survey_manager.subscribe(sub)

# ResponsesSurvey event declaration
_rs_subscribers = [LoggerResponsesSurveyNotifier(),
                   MindBoxResponsesSurveyNotifier()]
responses_survey_manager = ResponsesSurveyManager()
for sub in _rs_subscribers:
    responses_survey_manager.subscribe(sub)
