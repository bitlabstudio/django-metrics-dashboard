"""Views of the ``django-metrics-dashboard`` app."""
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from metrics_dashboard.decorators import permission_required
from metrics_dashboard.widget_pool import dashboard_widget_pool


class PermissionRequiredViewMixin(object):
    @method_decorator(
        permission_required('metrics_dashboard.can_view_dashboard'))
    def dispatch(self, request, *args, **kwargs):
        return super(PermissionRequiredViewMixin, self).dispatch(
            request, *args, **kwargs)


class DashboardView(PermissionRequiredViewMixin, TemplateView):
    template_name = 'metrics_dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data(**kwargs)
        ctx.update({
            'widgets': dashboard_widget_pool.get_widgets(),
        })
        return ctx


class DashboardAPIWidgetView(PermissionRequiredViewMixin, TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.widget = dashboard_widget_pool.widgets[kwargs.get('widget_name')]
        return super(DashboardAPIWidgetView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(DashboardAPIWidgetView, self).get_context_data(**kwargs)
        ctx.update(self.widget.get_context_data())
        return ctx

    def get_template_names(self):
        return [self.widget.template_name, ]
