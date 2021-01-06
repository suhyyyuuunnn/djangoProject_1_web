from django.urls import path
from .views import intro, home, new, create, show, edit, update, delete


app_name = "posts"
urlpatterns = [
    path('home/', home, name="home"),
    path('intro/', intro, name="intro"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('show/<int:post_id>/', show, name="show"),
    path('edit/<int:post_id>/', edit, name="edit"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:post_id>', delete, name="delete"),
]
