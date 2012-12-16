"""Base DashboardWidget of the ``django-metrics-dashboard`` app."""


class DashboardWidgetBase(object):
    """All DashboardWidgets must inherit this base class."""
    def get_context_data(self):
        """
        Should return a dictionary of template context variables.

        """
        return {}

    def get_name(self):
        """Returns the class name of this widget."""
        return self.__class__.__name__

    def update_widget_data(self):
        """
        Implement this in your widget in order to update the widget's data.

        This is the place where you would call some third party API, retrieve
        some data and save it into your widget's model.

        """
        raise NotImplementedError()
