from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('signout', views.signout),

    path('add', views.add),
    path('remove/<int:item_id>', views.deleteItem)
]