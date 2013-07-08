from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'guide.views.home', name='home'),
)
