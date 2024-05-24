from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework import generics, status
from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectDeleteAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDestroyAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client_name = self.request.data.get('client')
        if not client_name:
            raise ValidationError({"client": "This field is required."})

        # Try to get the client or create a new one if it doesn't exist
        try:
            client = Client.objects.get(client_name=client_name)
        except Client.DoesNotExist:
            client = Client.objects.create(client_name=client_name, created_by=self.request.user)

        user_ids = self.request.data.get('users', [])
        users = User.objects.filter(id__in=user_ids)

        serializer.save(
            created_by=self.request.user,
            client=client,
            users=users
        )

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

