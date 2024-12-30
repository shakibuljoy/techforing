from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project,Comment, Task, Member

userModel = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = ['id', 'username','password', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        user = userModel.objects.create_user(**validated_data)
        return user 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  


class CommentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'