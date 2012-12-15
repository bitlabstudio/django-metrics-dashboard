"""Factories for the ``django-metrics-dashboard`` app."""
import factory

from metrics_dashboard.models import DashboardWidgetSettings


class DashboardWidgetSettingsFactory(factory.Factory):
    FACTORY_FOR = DashboardWidgetSettings

    widget_name = 'my_widget'
    setting_name = 'my_setting'
    value = '1'
