"""Widget Pool for the ``django-metrics-dashboard`` app."""
from django.core.exceptions import ImproperlyConfigured

from django_load.core import load

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
        self.discovered = False

    def discover_widgets(self):
        """
        Searches for widgets in all INSTALLED_APPS.

        This will be called when you call ``get_all_widgets`` for the first
        time.

        """
        if self.discovered:
            return
        load('dashboard_widgets')
        self.discovered = True

    def get_widgets(self):
        """Discovers all widgets and returns them."""
        self.discover_widgets()
        return self.widgets

    def register_widget(self, widget_cls):
        """
        Registers the given widget.

        Widgets must inherit ``DashboardWidgetBase`` and you cannot register
        the same widget twice.

        :widget_cls: A class that inherits ``DashboardWidgetBase``.

        """
        if not issubclass(widget_cls, DashboardWidgetBase):
            raise ImproperlyConfigured(
                'DashboardWidgets must be subclasses of DashboardWidgetBase,'
                ' {0} is not.'.format(widget_cls))

        widget = widget_cls()
        widget_name = widget.get_name()
        if widget_name in self.widgets:
            raise WidgetAlreadyRegistered(
                'Cannot register {0}, a plugin with this name {1} is already '
                'registered.'.format(widget_cls, widget_name))

        self.widgets[widget_name] = widget

    def unregister_widget(self, widget_cls):
        """Unregisters the given widget."""
        if widget_cls.__name__ in self.widgets:
            del self.widgets[widget_cls().get_name()]


dashboard_widget_pool = DashboardWidgetPool()
