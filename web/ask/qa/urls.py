from django.conf.urls import url
from .import views

app_name = "qa"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url('', views.test),
    url('login/', views.test),
    url('signup/', views.test),
    url(r'question/(?P<group_id>[^/]+)', views.test),
    url('ask/',  views.test),
    url('popular/', views.test),
    url('new/', views.test),
]