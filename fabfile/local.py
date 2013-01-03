"""Fabric task that eases development of the project."""
from fabric.api import local

from .fabric_settings import PROJECT_NAME


def flake8():
    """Runs flake8 check against all files."""
    local('flake8 --statistics metrics_dashboard/.')


def test():
    """Runs the tests."""
    local('./{0}/tests/runtests.py'.format(PROJECT_NAME))
