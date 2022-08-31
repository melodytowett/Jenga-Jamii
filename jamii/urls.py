from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'jamii'
urlpatterns =[
  path('volunteer/',views.volunteer_list),
  path('volunteer/<int:pk>',views.volunteer_detail)
]