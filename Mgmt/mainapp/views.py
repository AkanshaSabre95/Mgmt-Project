from django.shortcuts import render
from rest_framework import viewsets
from .models import School,Student
from .serializer import SchoolSerializer,StudentSerializer

class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all
    serializer_class =SchoolSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all
    serializer_class = StudentSerializer


