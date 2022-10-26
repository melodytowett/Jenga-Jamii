from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import StudentList,StudentDescription
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    re_path(r'^api/student/$',views.StudentList.as_view()),
    re_path(r'^api-token-auth/', obtain_auth_token),
    re_path(r'api/student/student-id/(?P<pk>[0-9]+)/$',
        views.StudentDescription.as_view())
]