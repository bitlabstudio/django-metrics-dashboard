"""Base DashboardWidget of the ``django-metrics-dashboard`` app."""
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import datetime, now

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

    update_interval = 3600

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

    def set_last_update(self):
        """Sets the ``LAST_UPDATE`` setting to ``now()``."""
        self.save_setting('LAST_UPDATE', now().strftime(self.time_format))

    def should_update(self):
        """
        Checks if an update is needed.

        Checks against ``self.update_interval`` and the ``LAST_UPDATE`` setting
        if update is needed.

        """
        last_update = self.get_setting('LAST_UPDATE')
        if not last_update:
            last_update = datetime(1900, 1, 1)
        else:
            last_update = datetime.strptime(
                last_update.value, self.time_format)
        time_since = now() - last_update
        if time_since.seconds < self.update_interval:
            return False
        return True

    def update_widget_data(self):
        """
        Implement this in your widget in order to update the widget's data.

        This is the place where you would call some third party API, retrieve
        some data and save it into your widget's model.

        """
        raise NotImplementedError
