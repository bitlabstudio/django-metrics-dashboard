"""Views of the ``django-metrics-dashboard`` app."""
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'metrics_dashboard/dashboard.html'
