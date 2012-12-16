"""
DummyWidget implementation used by the tests.

"""
from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.widget_pool import dashboard_widget_pool


class DummyWidget(DashboardWidgetBase):
    """This widget is used by the tests."""
    pass


class DummyWidget2(DashboardWidgetBase):
    """This widget is used by the tests."""
    pass


dashboard_widget_pool.register_widget(DummyWidget)
dashboard_widget_pool.register_widget(DummyWidget2)
