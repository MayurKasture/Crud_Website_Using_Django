from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login page"),
    path('crud/', views.create_read, name="create_&_read_data"),
    path('delete/<int:id>/', views.delete_data, name="delete_data"),
    path('<int:id>/', views.update_data, name="update_data"),
]
