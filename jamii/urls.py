from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'jamii'
urlpatterns =[
  path('volunteer/',views.volunteer_list),
  path('volunteer/<int:pk>',views.volunteer_detail),
  path('contact/',views.contact_list),
  path('contact/<int:pk>',views.contact_detail),
  path('blood/',views.blood_list),
  path('blood/<int:pk>',views.blood_detail)
]