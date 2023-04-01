from rest_framework import serializers
from API.models import *

class StudentMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMainModel
        fields = '__all__'
        
class StudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentMarksModel
        fields = '__all__'
        
class StudentMarksMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentMarksMainModel
        fields = '__all__'