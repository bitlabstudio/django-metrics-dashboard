"""Decorators for the ``django-metrics-dashboard`` app."""
from django.conf import settings
from django.contrib.auth.decorators import (
    user_passes_test,
)
from django.core.exceptions import PermissionDenied

from metrics_dashboard import settings as app_settings


def permission_required(perm, login_url=None, raise_exception=False):
    """
    Re-implementation of the ``permission_required`` decorator, honors settings.

    If ``DASHBOARD_REQUIRE_LOGIN`` is False, this decorator will always return
    ``True``, otherwise it will check for the permission as usual.

    """
    def check_perms(user):
        if not getattr(
            settings, 'DASHBOARD_REQUIRE_LOGIN', app_settings.REQUIRE_LOGIN):
            return True
        # First check if the user has the permission (even anon users)
        if user.has_perm(perm):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url=login_url)
