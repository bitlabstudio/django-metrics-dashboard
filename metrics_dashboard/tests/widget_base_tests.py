"""Tests for the widget base class of the ``django-metrics-dashboard`` app."""
from django.test import TestCase

from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.tests.test_widget_app.dashboard_widgets import (
    DummyWidget,
)


class DashboardWidgetBaseTestCase(TestCase):
    """Tests for the ``DashboardWidgetBase`` base class."""
    def test_get_context_data(self):
        """get_context_data should return an empty dictionary by default."""
        base = DashboardWidgetBase()
        result = base.get_context_data()
        self.assertEqual(result, {})

    def test_get_name(self):
        """
        get_name should return the class name when called on a child class.

        """
        widget = DummyWidget()
        result = widget.get_name()
        self.assertEqual(result, 'DummyWidget')

    def test_update_widget_data_not_implemented(self):
        """update_widget_data should throw exception if not implemented."""
        base = DashboardWidgetBase()
        self.assertRaises(NotImplementedError, base.update_widget_data)
