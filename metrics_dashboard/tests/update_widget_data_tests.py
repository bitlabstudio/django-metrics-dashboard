"""Tests for the ``update_widget_data`` admin command."""
from django.core.management import call_command
from django.test import TestCase


class UpdateWidgetDataTestCase(TestCase):
    """Tests for the ``update_widget_data`` admin command."""
    def test_command(self):
        """update_widget_data should run without errors"""
        call_command('update_widget_data')
