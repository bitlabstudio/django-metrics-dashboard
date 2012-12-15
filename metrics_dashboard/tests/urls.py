"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into your main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('',
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='auth_login'),

    url(r'^', include('metrics_dashboard.urls')),
)
