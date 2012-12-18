"""URLs for the ``django-metrics-dashboard`` app."""
from django.conf.urls.defaults import patterns, url

from metrics_dashboard.views import DashboardView, DashboardAPIWidgetView


urlpatterns = patterns(
    '',
    url(r'^$',
        DashboardView.as_view(),
        name='dashboard_view',),

    url(r'^api/widget/(?P<widget_name>\w+)/',
        DashboardAPIWidgetView.as_view(),
        name='dashboard_api_widget',),
)
