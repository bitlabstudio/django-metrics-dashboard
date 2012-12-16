"""Tests for the views of the ``django-metrics-dashboard`` app."""
from django.test import TestCase
from django.test.client import RequestFactory

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from metrics_dashboard.tests.mixins import WidgetTestCaseMixin
from metrics_dashboard.views import DashboardView, DashboardAPIWidgetView


class DashboardViewTestMixin(object):
    def setUp(self):
        super(DashboardViewTestMixin, self).setUp()
        self.factory = RequestFactory()
        self.request = self.factory.get(self.get_url())
        self.request.user = UserFactory()


class DashboardAPIWidgetViewTestCase(WidgetTestCaseMixin,
                                     DashboardViewTestMixin, ViewTestMixin,
                                     TestCase):
    """Tests for the ``DashboardAPIWidgetView`` view class."""
    def get_view_kwargs(self):
        return {
            'widget_name': 'DummyWidget',
        }

    def get_view_name(self):
        return 'dashboard_api_widget'

    def test_view(self):
        """api view should return the correct template and context"""
        kwargs = self.get_view_kwargs()
        response = DashboardAPIWidgetView().dispatch(self.request, **kwargs)
        self.assertTrue('value' in response.context_data)


class DashboardViewTestCase(WidgetTestCaseMixin, DashboardViewTestMixin,
                            ViewTestMixin, TestCase):
    def get_view_name(self):
        return 'dashboard_view'

    def test_view_anonymous(self):
        """View should be callable for anonymous users."""
        self.should_be_callable_when_anonymous()

    def test_view_login_required(self):
        """View should not be callable for anonymous if REQUIRE_LOGIN==True."""
        with self.settings(DASHBOARD_REQUIRE_LOGIN=True):
            self.should_redirect_to_login_when_anonymous()

    def test_get_context_data(self):
        """View should add all registered widgets to the context."""
        self._unregister_widgets()
        response = DashboardView().dispatch(self.request)
        self.assertTrue('widgets' in response.context_data)
