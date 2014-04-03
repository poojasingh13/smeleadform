from django.conf.urls.defaults import *


from leadform import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
