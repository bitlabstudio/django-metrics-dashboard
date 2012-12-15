"""Views of the ``django-metrics-dashboard`` app."""
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from metrics_dashboard.decorators import permission_required


class DashboardView(TemplateView):
    template_name = 'metrics_dashboard/dashboard.html'

    @method_decorator(
        permission_required('metrics_dashboard.can_view_dashboard'))
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)
