from django.urls import path
from .views import *


urlpatterns = [
   path('register/', Register, name="Register"),
   path('login/', Login, name="Login"),
   path('logout/', logout_user, name="logout"),
]