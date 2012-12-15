"""Models for the ``django-metrics-dashboard`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DashboardWidgetSettings(models.Model):
    """
    Table that can hold all settings for all widgets.

    :widget_name: This should be a name that uniquely identifies a widget.
    :setting_name: This is the name of the setting to be saved.
    :value: This is the value of the setting.
    """
    class Meta:
        unique_together = ('widget_name', 'setting_name', )

        # This permission is actually not relevant to the model but defines if
        # a user has access to the dashboard view. It's just added to this
        # model for convenience, it could just as well be on any other model.
        permissions = (
            ('can_view_dashboard', 'Can view the dashboard'),
        )

    widget_name = models.CharField(
        max_length=128,
        verbose_name=_('Widget name'),
    )

    setting_name = models.CharField(
        max_length=128,
        verbose_name=_('Setting name'),
    )

    value = models.CharField(
        max_length=4000,
        verbose_name=_('Setting name'),
    )

    def __unicode__(self):
        return '{0} of {1}'.format(self.setting_name, self.widget_name)
