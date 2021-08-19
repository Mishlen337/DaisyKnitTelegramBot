"""Module to declare responses survey manager."""

from contracts import contract
from typing import Set
from notifiers.abstracts import AbstractResponsesSurveyObserver,\
                                AbstractNotificationManager


class ResponsesSurveyManager(AbstractNotificationManager):
    """"Manager to notify about responses to a survey."""
    def __init__(self):
        self.__subscribers: Set[AbstractResponsesSurveyObserver] = set()

    @contract
    def subscribe(self, subscriber):
        """Subscribes observer to handle responses to a survey event.

        :param subscriber: observer
        :type subscriber: [type]
        """
        self.__subscribers.add(subscriber)

    @contract
    def unsubscribe(self, subscriber):
        """Unsubscribes observer to handle responses to a survey event.

        :param subscriber: observer
        :type subscriber: [type]
        """
        self.__subscribers.remove(subscriber)
        # TODO Handle Key Error

    @contract
    async def notify(self, event_args):
        """Notifies observers of responses to a survey event.

        :param event_args: observer
        :type event_args: [type]
        """
        for subscriber in self.__subscribers:
            await subscriber.update(event_args)
