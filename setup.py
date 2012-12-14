import os
from setuptools import setup, find_packages
import metrics_dashboard


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-metrics-dashboard",
    version=metrics_dashboard.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, reusable, metrix, dashboard',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/django-metrics-dashboard",
    packages=find_packages(),
    include_package_data=True,
)
