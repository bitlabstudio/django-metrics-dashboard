"""
DummyWidget implementation used by the tests.

"""
from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.widget_pool import dashboard_widget_pool


class DummyWidget(DashboardWidgetBase):
    """This widget is used by the tests."""
    template_name = 'test_widget_app/dummy_widget.html'

    def get_context_data(self):
        return {
            'value': 'Foobar',
        }

    def update_widget_data(self):
        pass


class DummyWidget2(DashboardWidgetBase):
    """This widget is used by the tests."""
    template_name = 'test_widget_app/dummy_widget2.html'

    def get_context_data(self):
        return {
            'value': 'Barfoo',
        }

    def update_widget_data(self):
        pass


dashboard_widget_pool.register_widget(DummyWidget)
dashboard_widget_pool.register_widget(DummyWidget2)
