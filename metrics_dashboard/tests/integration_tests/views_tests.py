"""Tests for the views of the ``django-metrics-dashboard`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin


class DasboardViewTestCase(ViewTestMixin, TestCase):
    def get_view_name(self):
        return 'dashboard_view'

    def test_view(self):
        self.should_be_callable_when_anonymous()

        with self.settings(DASHBOARD_REQUIRE_LOGIN=True):
            self.should_redirect_to_login_when_anonymous()
