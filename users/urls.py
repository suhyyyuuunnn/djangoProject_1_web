from django.urls import path
from .views import signup, login, logout


app_name = "users"
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signup/', logout, name='logout'),
]
