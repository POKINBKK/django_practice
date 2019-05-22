from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='my_login'),
    path('logout/', views.my_logout, name='my_logout'),
    path('createpost/', views.createpost, name='createpost')
]