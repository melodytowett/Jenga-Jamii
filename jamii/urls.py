from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'jamii'
urlpatterns =[

  path('api/volunteer/',views.Volunteer.as_view()),
  path('api-auth/',include('rest_framework.urls'))
]