from django.conf.urls import url

from demoapp.views import index


urlpatterns =[
    url(r'^index/$', index, name = "index"),
]