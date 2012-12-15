Django Metrics Dashboard
========================

DO NOT USE THIS! THIS IS AN EARLY ALPHA AND DOES NOT WORK!

A reusable Django app that allows you to display a dashboard with any number
of widgets to show any data you care about. The widets are updated via
socket.io, so you never need to refresh your dashboard.

Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django 1.4.3
* South

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-metrics-dashboard

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-metrics-dashboard.git#egg=metrics_dashboard

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'metrics_dashboard',
    ]

Hook the app into your main ``urls.py``::

    urlpatterns += patterns('',
        ...
        url(r'^dashboard/', include('metrics_dashboard.urls')),
    )

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate metrics_dashboard


Settings
--------

DASHBOARD_REQUIRE_LOGIN
+++++++++++++++++++++++

*Default*: ``True``

When you set this to false, anyone can access the dashboard. If you are
displaying sensitive metrics, you might want to leave this at ``True``.


Usage
-----

For now: Install it and go visit the URL :) More features coming soon.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-metrics-dashboard
    $ pip install -r requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch


Testing
-------

If you want to contribute to this project you can run the tests without setting
up a Django project. Just clone this repository and execute the
``runtests.py``::

    $ ./metrics_dashboard/tests/runtests.py

Sometimes a new feature needs new South migrations, in this case you should
do the following::

    $ rm db.sqlite
    $ ./manage.py syncdb --migrate
    $ ./manage.py schemamigration metrics_dashboard --auto


Compiling the CSS files
-----------------------

If you want to make changes to the CSS files, please edit the files
``metrics-dashboard-variables.less``, ``styles.less`` and
``responsive-styles.less``. Then run ``fab lessc`` from the root of the
project.

If you want to setup a file system watcher and compile the ``.css`` files
automagically, just execute ``./watchmedo-less.sh``.


Discuss
-------

If you have questions or issues, please open an issue on GitHub.

If we don't react quickly, please don't hesitate to ping me on Twitter
(`@mbrochh <https://twitter.com/mbrochh>`_)
