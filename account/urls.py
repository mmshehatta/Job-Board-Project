from django.urls import include, path

from . import views


app_name='accounts'

urlpatterns = [
    path('signup',views.signUp , name='signup'),
    path('profile',views.profile , name='profile'),
   ]