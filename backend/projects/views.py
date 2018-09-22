from django.shortcuts import render

# Create your views here.
from projects.models import Project, Stack
from rest_framework import viewsets
from projects.serializers import ProjectSerializer, StackSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class StackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Stack.objects.all()
    serializer_class = StackSerializer