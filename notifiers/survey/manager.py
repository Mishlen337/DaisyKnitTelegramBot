"""Module to declare survey manager"""

from typing import Set
from contracts import contract
from notifiers.abstracts import AbstractNotificationManager,\
                                AbstractSurveyObserver


class SurveyManager(AbstractNotificationManager):
    """Manager to notify about a survey."""

    def __init__(self):
        self.__subscribers: Set[AbstractSurveyObserver] = set()

    @contract
    def subscribe(self, subscriber: AbstractSurveyObserver):
        """Subscribes observer to handle a survey event.

        :param subscriber: observer
        :type subscriber: AbstractSurveyObserver
        """
        self.__subscribers.add(subscriber)

    @contract
    def unsubscribe(self, subscriber: AbstractSurveyObserver):
        """Unsubscribes observer to handle a survey event.

        :param subscriber: observer
        :type subscriber: AbstractSurveyObserver
        """
        self.__subscribers.remove(subscriber)
        # TODO handle Key Error

    @contract
    async def notify(self, event_args):
        """Notifies observers of a survey event.

        :param event_args: data of an event
        :type event_args: [type]
        """
        for subscriber in self.__subscribers:
            await subscriber.update(event_args)
