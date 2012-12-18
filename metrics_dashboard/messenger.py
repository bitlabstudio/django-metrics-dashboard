"""Utility functions to send messages to ``django-socketio-messenger``."""
import requests

from django.conf import settings


def broadcast_channel(channel, message):
    """
    Forwards a message to your ``django-socketio-messenger`` installation.

    """
    url = settings.DASHBOARD_MESSENGER_URL
    payload = {'channel': channel, 'message': message, }
    response = requests.post(url, data=payload)
    return response
