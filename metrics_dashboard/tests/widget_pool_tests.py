"""Tests for the Widget Pool of the ``django-metrics-dashboard`` app."""
from django.test import TestCase

from django.core.exceptions import ImproperlyConfigured
from metrics_dashboard.exceptions import WidgetAlreadyRegistered
from metrics_dashboard.tests.mixins import WidgetTestCaseMixin
from metrics_dashboard.tests.test_app.dashboard_widgets import DummyWidget
from metrics_dashboard.widget_pool import (
    DashboardWidgetPool,
    dashboard_widget_pool,
)


class FalseWidget(object):
    """
    This class will not be accepted as a widget.

    Because it does not inherit ``WidgetBase``.

    """
    pass


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
        register_widget should raise exception if widget does not inherit

        ``DashboardWidgetBase``.

        """
        self.assertRaises(
            ImproperlyConfigured, dashboard_widget_pool.register_widget,
            FalseWidget)

    def test_register_widget(self):
        """register_widget should add the widget to ``self.widgets``."""
        self._unregister_widgets()
        dashboard_widget_pool.register_widget(DummyWidget)
        self.assertTrue('DummyWidget' in dashboard_widget_pool.widgets)

    def test_register_already_registered(self):
        """
        register_widget should raise exception if widget is already registered.

        """
        self._unregister_widgets()
        dashboard_widget_pool.register_widget(DummyWidget)
        self.assertRaises(
            WidgetAlreadyRegistered, dashboard_widget_pool.register_widget,
            DummyWidget)

    def test_unregister_widget(self):
        """
        unregister_widget should be remove the widget from ``self.widgets``.

        """
        self._unregister_widgets()
        dashboard_widget_pool.register_widget(DummyWidget)
        dashboard_widget_pool.unregister_widget(DummyWidget)
        self.assertEqual(dashboard_widget_pool.widgets, {})

    def test_1_discover_widgets(self):
        """
        discover_widgets Should find widgets in INSTALLED_APPS.

        When called again, it should not nothing.

        This test must be executed first before any other test messes around
        with the registered widgets.

        """
        dashboard_widget_pool.discover_widgets()
        self.assertTrue('DummyWidget' in dashboard_widget_pool.widgets)
        self.assertTrue('DummyWidget2' in dashboard_widget_pool.widgets)

        dashboard_widget_pool.discover_widgets()
        self.assertTrue('DummyWidget' in dashboard_widget_pool.widgets)
        self.assertTrue('DummyWidget2' in dashboard_widget_pool.widgets)

    def test_get_widgets(self):
        """get_widgets should discover widgets and return them."""
        widgets = dashboard_widget_pool.get_widgets()
        self.assertEqual(widgets, dashboard_widget_pool.widgets)
