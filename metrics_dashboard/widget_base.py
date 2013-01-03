"""Base DashboardWidget of the ``django-metrics-dashboard`` app."""
from django.utils.translation import ugettext_lazy as _

from metrics_dashboard.models import DashboardWidgetSettings


class DashboardWidgetBase(object):
    """All DashboardWidgets must inherit this base class."""
    base_settings = {
        'IS_ENABLED': {
            'verbose_name': _('Is enabled'),
        },
        'LAST_UPDATE': {
            'verbose_name': _('Last update'),
        }
    }

    settings = {}

    def get_context_data(self):
        """
        Should return a dictionary of template context variables.

        """
        return {
            'widget_name': self.get_name(),
        }

    def get_name(self):
        """Returns the class name of this widget."""
        return self.__class__.__name__

    def get_setting(self, setting_name, default=None):
        """
        Returns the setting for this widget from the database.

        :setting_name: The name of the setting.
        :default: Optional default value if the setting cannot be found.

        """
        try:
            setting = DashboardWidgetSettings.objects.get(
                widget_name=self.get_name(),
                setting_name=setting_name)
        except DashboardWidgetSettings.DoesNotExist:
            setting = default
        return setting

    def save_setting(self, setting_name, value):
        """Saves the setting value into the database."""
        setting = self.get_setting(setting_name)
        if setting is None:
            setting = DashboardWidgetSettings.objects.create(
                widget_name=self.get_name(),
                setting_name=setting_name,
                value=value)
        setting.value = value
        setting.save()
        return setting

    def update_widget_data(self):
        """
        Implement this in your widget in order to update the widget's data.

        This is the place where you would call some third party API, retrieve
        some data and save it into your widget's model.

        """
        raise NotImplementedError()
