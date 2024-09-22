from concurrent.futures import ThreadPoolExecutor

import requests
from django.conf import settings
from rest_framework import serializers

from .models import Users, Questions, Answer, Summary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'full_name', 'password', 'phone_number', 'age')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=14)
    password = serializers.CharField(required=True)


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'question', 'question_audio')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer', 'user', 'answer_audio')



class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id', 'user', 'summary_audio', 'summary')
