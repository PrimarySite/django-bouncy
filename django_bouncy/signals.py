"""Signals from the django_bouncy app"""
# pylint: disable=invalid-name
from django.dispatch import Signal

# Any notification received
notification = Signal(["notification", "request"])

# New SubscriptionConfirmation received
subscription = Signal(["result", "notification"])

# New bounce or complaint received
feedback = Signal(["instance", "message", "notification"])
