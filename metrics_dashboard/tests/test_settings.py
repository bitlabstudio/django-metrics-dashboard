"""Settings that need to be set in order to run the tests."""
from settings import *

INSTALLED_APPS.remove('metrics_dashboard.tests.test_widget_app')
INSTALLED_APPS.append('test_widget_app')
