from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.addItem),
    path('channel/',views.getChannel),
    path('channel/<str:channel>/',views.getTitles),
    path('channel/<str:channel>/<str:date>/',views.getTitlesDate),
    path('channel/<str:channel>/<str:start_date>/<str:end_date>/',views.getTitlesDateRange),
]