"""Tests for the views of the ``django-metrics-dashboard`` app."""
from django.test import TestCase
from django.test.client import RequestFactory

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from metrics_dashboard.tests.mixins import WidgetTestCaseMixin
from metrics_dashboard.views import DashboardView


class DashboardViewTestCase(WidgetTestCaseMixin, ViewTestMixin, TestCase):
    def setUp(self):
        super(DashboardViewTestCase, self).setUp()
        self.factory = RequestFactory()

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
        request = self.factory.get(self.get_url())
        request.user = UserFactory()
        response = DashboardView.as_view()(request)
        self.assertTrue('widgets' in response.context_data)
