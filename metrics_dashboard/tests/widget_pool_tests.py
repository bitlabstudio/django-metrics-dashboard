"""Tests for the Widget Pool of the ``django-metrics-dashboard`` app."""
from django.test import TestCase

from django.core.exceptions import ImproperlyConfigured
from metrics_dashboard.exceptions import WidgetAlreadyRegistered
from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.widget_pool import (
    DashboardWidgetPool,
    dashboard_widget_pool,
)


class DummyWidget(DashboardWidgetBase):
    """This widget can be registered for testing purposes."""
    pass


class FalseWidget(object):
    """
    This class will not be accepted as a widget.

    Because it does not inherit ``WidgetBase``.

    """
    pass


class WidgetTestCaseMixin(object):
    def tearDown(self):
        # unregister all widgets
        dashboard_widget_pool.widgets = {}


class DashboardWidgetPoolTestCase(WidgetTestCaseMixin, TestCase):
    """Tests for the ``WidgetPool`` class."""
    longMessage = True

    def test_instantiates_on_import(self):
        """
        Should instantiate WidgetPool when module is imported.

        """
        self.assertEqual(
            dashboard_widget_pool.__class__, DashboardWidgetPool, msg=(
                'When importing from `widget_pool`, an instance of'
                ' `WidgetPool` should be created'))

    def test_register_false_widget(self):
        """
        Should raise exception if the widget not inherit `DashboardWidgetBase`

        """
        self.assertRaises(
            ImproperlyConfigured, dashboard_widget_pool.register_widget,
            FalseWidget)

    def test_register_widget(self):
        """Should add the widget to ``self.widgets``."""
        dashboard_widget_pool.register_widget(DummyWidget)
        self.assertTrue('DummyWidget' in dashboard_widget_pool.widgets)

    def test_register_already_registered(self):
        """Should raise exception if the widget is already registered."""
        dashboard_widget_pool.register_widget(DummyWidget)
        self.assertRaises(
            WidgetAlreadyRegistered, dashboard_widget_pool.register_widget,
            DummyWidget)

    def test_unregister_widget(self):
        """
        When unregistering a widget it should be removed from ``self.widgets``.

        """
        dashboard_widget_pool.register_widget(DummyWidget)
        dashboard_widget_pool.unregister_widget(DummyWidget)
        self.assertEqual(dashboard_widget_pool.widgets, {})
