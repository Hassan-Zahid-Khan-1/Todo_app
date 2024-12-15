from django.urls import path
from .views import *
urlpatterns = [
    path('todo/',home ,name="home"),
    path("delete_todo/<int:delete_id>/",delete_todo,name="delete_todo"),
     path("update_todo/<int:update_id>/",update_todo,name="update_todo"),
]
