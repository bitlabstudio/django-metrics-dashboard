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


DASHBOARD_MESSENGER_URL
+++++++++++++++++++++++

*Default*: No default, you have to set this.

Set this to the API endpoint of your ``django-socketio-messenger``
installation. A valid value should look like this::

    http://<IP>:<PORT>/broadcast_channel/

We need this because all messages going through socketio must be sent from
the same process. However, this app needs to broadcast messages from an
admin command which get's executed from a cron job, therefore that command
would be a different process than your wsgi process. As a simple (silly and
hackish) solution we created `django-socketio-messenger <https://github.com/bitmazk/django-socketio-messenger>`_
which is really just another mini Django app that functions as your socket.io
server. Therefore this app would send HTTP requests to your
``django-socketio-messenger`` which then would broadcast those messages to
your connected socket.io subscribers.


Usage
-----

For now: Install it and go visit the URL :) More features coming soon.


Creating widgets
----------------

* Create a new Django app. Per convention, you should call your app something
  like ``dashboardwidget_yourwidgetname``. This way we can easily search
  PyPi for ``dashboardwidget`` and will find all widgets that have been
  published.
* Give it a file ``dashboard_widget.py``
* Implement your widget. It should inherit ``DashboardWidgetBase``
* Your widget needs the following implementations:
  * a ``template_name`` attribute, just like any Django view
  * a ``get_context_data`` method. It should return a dictionary
    of template context variables
  * a ``update_widget_data`` method. It should get data from a 3rd party API
    and save it to the widget's model. THen it should send a message to the
    widget's socket.io channel so that the subscribed browsers know that the
    widget has new data and needs an update.
* Register your widget with the ``dashboard_widget_pool``.

Example ``dashboard_widgets.py``::

    from metrics_dashboard.widget_base import DashboardWidgetBase
    from metrics_dashboard.widget_pool import dashboard_widget_pool

    class DummyWidget(DashboardWidgetBase):
        """This widget is used by the tests."""
        template_name = 'dashboardwidget_dummy/dummy_widget.html'

        def get_context_data(self):
            return {
                'value': 'Foobar',
            }

        def update_widget_data(self):
            # TODO: add example implementation here.

    dashboard_widget_pool.register_widget(DummyWidget)


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
