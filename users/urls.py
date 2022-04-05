# from django.urls import path
# from .views import SignUpView

# app_name = 'users'

# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
# ]


from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),

]

