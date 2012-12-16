"""Views of the ``django-metrics-dashboard`` app."""
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from metrics_dashboard.decorators import permission_required
from metrics_dashboard.widget_pool import dashboard_widget_pool


class DashboardView(TemplateView):
    template_name = 'metrics_dashboard/dashboard.html'

    @method_decorator(
        permission_required('metrics_dashboard.can_view_dashboard'))
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data(**kwargs)
        ctx.update({
            'widgets': dashboard_widget_pool.get_widgets(),
        })
        return ctx
