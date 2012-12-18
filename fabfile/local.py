"""Fabric task that eases development of the project."""
from fabric.api import local

from .fabric_settings import PROJECT_NAME


def flake8():
    """Runs flake8 check against all files."""
    local('flake8 --statistics metrics_dashboard/.')


def lessc():
    """Compiles all less files."""
    local('lessc {0}/static/{0}/css/bootstrap.less'
          ' {0}/static/{0}/css/bootstrap.css'.format(PROJECT_NAME))
    local('lessc {0}/static/{0}/css/responsive.less'
          ' {0}/static/{0}/css/bootstrap-responsive.css'.format(PROJECT_NAME))


def test():
    """Runs the tests."""
    local('./{0}/tests/runtests.py'.format(PROJECT_NAME))
