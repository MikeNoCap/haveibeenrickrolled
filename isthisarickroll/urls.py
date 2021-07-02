from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path("", views.home_re),
    path("home/", views.lol),
    path("result-ok/", views.rick_ok),
    path("result-bad/", views.rick_not_ok),
    path("report-rickroll/", views.report_link)
    ]