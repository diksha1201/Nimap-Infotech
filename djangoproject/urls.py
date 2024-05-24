"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nimapp.views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView, ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView,UserDeleteAPIView, ProjectDeleteAPIView,ClientDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
    path('clients/<int:id>/', ClientDestroyAPIView.as_view(), name='client-delete'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy'),
    # path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('users/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('projects/<int:pk>/', ProjectDeleteAPIView.as_view(), name='project-delete'),
]
