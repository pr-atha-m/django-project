
from app1 import views
from django.urls import path


app_name = 'app1'
urlpatterns = [

    path('models/' , views.users , name = 'users'),
    path('other/' , views.other , name = 'other') ,
    path('relative/' , views.relative , name = 'relative'),
    path('user_login/' , views.user_login , name = 'user_login'),


]