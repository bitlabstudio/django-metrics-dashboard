"""
DummyWidget implementation used by the tests.

"""
import datetime

from django.utils.translation import ugettext_lazy as _

from metrics_dashboard.messenger import broadcast_channel
from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.widget_pool import dashboard_widget_pool


class DummyWidget(DashboardWidgetBase):
    """This widget is used by the tests."""
    template_name = 'test_widget_app/dummy_widget.html'
    settings = {
        'VALUE': {
            'verbose_name': _('Value'),
        }
    }

    def get_context_data(self):
        ctx = super(DummyWidget, self).get_context_data()
        ctx.update({
            'value': self.get_setting('VALUE'),
        })
        return ctx

    def update_widget_data(self):
        self.save_setting('VALUE', str(datetime.datetime.now()))
        broadcast_channel(self.get_name(), 'update')


class DummyWidget2(DashboardWidgetBase):
    """This widget is used by the tests."""
    template_name = 'test_widget_app/dummy_widget2.html'

    def get_context_data(self):
        ctx = super(DummyWidget2, self).get_context_data()
        ctx.update({
            'value': 'Barfoo',
        })
        return ctx

    def update_widget_data(self):
        pass


dashboard_widget_pool.register_widget(DummyWidget)
dashboard_widget_pool.register_widget(DummyWidget2)
