"""Base DashboardWidget of the ``django-metrics-dashboard`` app."""


class DashboardWidgetBase(object):
    """All DashboardWidgets must inherit this base class."""
    def get_context_data(self):
        """
        Should return a dictionary of template context variables.

        """
        return {}

    def get_name(self):
        return self.__class__.__name__
