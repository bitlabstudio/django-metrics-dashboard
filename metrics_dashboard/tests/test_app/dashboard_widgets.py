"""
DummyWidget implementation used by the tests.

"""
from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.widget_pool import dashboard_widget_pool


class DummyWidget(DashboardWidgetBase):
    """DummyWidget implementation used by the tests."""
    pass


dashboard_widget_pool.register_widget(DummyWidget)
