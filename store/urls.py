from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('new-page/', views.new_page, name='new_page'),
    path('success/',views.success, name='success'),
    path('logout/', views.logout, name='logout'),
    path('departments/',views.departments)
]