from rest_framework import serializers
from .models import School,Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        field = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = '__all__'