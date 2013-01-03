"""Views of the ``django-metrics-dashboard`` app."""
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from metrics_dashboard.decorators import permission_required
from metrics_dashboard.widget_pool import dashboard_widget_pool


class PermissionRequiredViewMixin(object):
    """
    Mixin to protect a view and require ``can_view_dashboard`` permission.

    Permission will only be required if the ``DASHBOARD_REQUIRE_LOGIN``
    setting is ``True``.

    """
    @method_decorator(
        permission_required('metrics_dashboard.can_view_dashboard'))
    def dispatch(self, request, *args, **kwargs):
        return super(PermissionRequiredViewMixin, self).dispatch(
            request, *args, **kwargs)


class DashboardView(PermissionRequiredViewMixin, TemplateView):
    """
    Main view of the app. Displays the metrics dashboard.

    Widgets on the dashboard get loaded individually via AJAX calls against
    the ``DashboardAPIWidgetView``.

    It also loads socket.io and reloads an individual widget's template when
    the widget's data has been updated. This means, once this view is loaded,
    the page doesn't have to be refreshed at all. The widgets will simply
    update themselves.

    """
    template_name = 'metrics_dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data(**kwargs)
        widgets = dashboard_widget_pool.get_widgets()
        ctx.update({'widgets': widgets, })
        return ctx


class DashboardAPIWidgetView(PermissionRequiredViewMixin, TemplateView):
    """
    View to be called via AJAX. Returns the template of a widget.

    This allows us to update widgets individually whenever their data has been
    updated.

    """
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
