from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'guide.views.home', name='home'),
    url(r'^(?P<place_slug>[\w-]+)/overview/$', 'guide.views.overview', name='overview'),
    url(r'^(?P<place_slug>[\w-]+)/study/$', 'guide.views.study', name='study'),
    url(r'^(?P<place_slug>[\w-]+)/eat/$', 'guide.views.eat', name='eat'),
    url(r'^(?P<place_slug>[\w-]+)/play/$', 'guide.views.play', name='play'),
    url(r'^(?P<place_slug>[\w-]+)/do/$', 'guide.views.do', name='do'),
    url(r'^(?P<place_slug>[\w-]+)/tips/$', 'guide.views.tips', name='tips'),
    url(r'^(?P<place_slug>[\w-]+)/travel/$', 'guide.views.travel', name='travel'),
    url(r'^(?P<place_slug>[\w-]+)/weekend/$', 'guide.views.weekend', name='weekend'),
    url(r'^(?P<place_slug>[\w-]+)/contribute/$', 'guide.views.contribute', name='contribute'),
)
