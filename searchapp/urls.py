from django.urls import path
from . import views

app_name = 'searchapp'

urlpatterns = [
    path('result', views.searchresult, name='searchresult'),
]
