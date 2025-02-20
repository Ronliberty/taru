from django.urls import path
from .import views
from .views import role_based_redirect


app_name = 'account'
urlpatterns = [

    path('role-based-redirect/', role_based_redirect, name='role_based_redirect'),
 ]


