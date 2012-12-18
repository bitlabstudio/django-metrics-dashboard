"""Tests for the ``update_widget_data`` admin command."""
from django.core.management import call_command
from django.test import TestCase

from mock import patch

from metrics_dashboard.widget_pool import dashboard_widget_pool


class UpdateWidgetDataTestCase(TestCase):
    """Tests for the ``update_widget_data`` admin command."""
    def test_command(self):
        """update_widget_data should run without errors"""
        widget = dashboard_widget_pool.widgets['DummyWidget']
        with patch.object(widget, 'update_widget_data',
                          return_value=None) as mock_method:
            call_command('update_widget_data')
        mock_method.assert_called_once()
