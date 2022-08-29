from django.urls import path

from . import views
urlpatterns =[
  path('api/volunteer/',views.Volunteer.as_view())
]