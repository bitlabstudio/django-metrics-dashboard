"""Widget Pool for the ``django-metrics-dashboard`` app."""
from django.core.exceptions import ImproperlyConfigured

from metrics_dashboard.exceptions import WidgetAlreadyRegistered
from metrics_dashboard.widget_base import DashboardWidgetBase


class DashboardWidgetPool(object):
    """
    A pool of registered DashboardWidgets.

    This class should only be instantiated at the end of this file, therefore
    serving as a singleton. All other files should just import the instance
    created in this file.

    Inspired by
    https://github.com/divio/django-cms/blob/develop/cms/plugin_pool.py

    """
    def __init__(self):
        self.widgets = {}

    def register_widget(self, widget_cls):
        if not issubclass(widget_cls, DashboardWidgetBase):
            raise ImproperlyConfigured(
                'DashboardWidgets must be subclasses of DashboardWidgetBase,'
                ' {0} is not.'.format(widget_cls))

        widget_name = widget_cls.__name__
        if widget_name in self.widgets:
            raise WidgetAlreadyRegistered(
                'Cannot register {0}, a plugin with this name {1} is already '
                'registered.'.format(widget_cls, widget_name))

        self.widgets[widget_name] = widget_cls


dashboard_widget_pool = DashboardWidgetPool()
