from django.conf.urls.defaults import *
from zcms import views

urlpatterns = patterns('',
    (r'^setcontext', views.setContext),
    (r'^(.*)$', views.showPage),
)
