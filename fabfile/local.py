"""Fabric task that eases development of the project."""
from fabric.api import local

from .fabric_settings import PROJECT_NAME


def lessc():
    """Compiles all less files."""
    local('lessc {0}/static/{0}/css/bootstrap.less'
          ' {0}/static/{0}/css/bootstrap.css'.format(PROJECT_NAME))
    local('lessc {0}/static/{0}/css/responsive.less'
          ' {0}/static/{0}/css/bootstrap-responsive.css'.format(PROJECT_NAME))
