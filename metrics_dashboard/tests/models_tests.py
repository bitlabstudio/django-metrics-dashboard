"""Tests for the models of the ``django-metrics-dashboard`` app."""
from django.test import TestCase

from metrics_dashboard.tests.factories import DashboardWidgetSettingsFactory


class DashboardWidgetSettingsTestCase(TestCase):
    """Tests for the ``DashboardWidgetSettings`` model class."""
    longMessage = True

    def test_model(self):
        instance = DashboardWidgetSettingsFactory()
        self.assertTrue(instance.pk)
