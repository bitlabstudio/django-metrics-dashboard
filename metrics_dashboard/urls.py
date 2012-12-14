"""URLs for the ``django-metrics-dashboard`` app."""
from django.conf.urls.defaults import patterns, url

from metrics_dashboard.views import DashboardView


urlpatterns = patterns('',
    url(r'^$',
        DashboardView.as_view(),
        name='dashboard_view',
    ),
)
