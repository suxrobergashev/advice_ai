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

    def create(self, validated_data):
        # Check if 'answer_audio' is present
        if 'answer_audio' in validated_data:
            audio_file = validated_data['answer_audio']

            # Make a request to the external API to process the audio
            response = self.process_audio(audio_file)

            # Assume the API returns the answer as a JSON object with 'text' key
            try:
                response_data = response.json()
                validated_data['answer'] = response_data.get('text')
            except Exception as e:
                raise serializers.ValidationError("Failed to process the audio")

        # If 'answer' is already provided, it will be used as is
        return super().create(validated_data)

    def process_audio(self, audio_file):
        """
        Helper method to send the audio file to an external API for processing.
        This method assumes that the API accepts a POST request with a file and returns a text response.
        """
        url = f'{settings.BASE_URL}/apis/stt/post/'
        files = {'audio': ('tim_original.mp3', audio_file.read(), 'audio/mpeg')}

        try:
            response = requests.post(url, files=files)
            print(response.text)
            return response
        except requests.RequestException as e:
            raise serializers.ValidationError(f"API request failed: {e}")

    # def create(self, validated_data):
    #     # Save the initial answer with placeholder for the audio transcription
    #     answer = super().create(validated_data)
    #
    #     # Check if 'answer_audio' is present
    #     if 'answer_audio' in validated_data:
    #         audio_file = validated_data['answer_audio']
    #
    #         # Process audio asynchronously
    #         with ThreadPoolExecutor() as executor:
    #             future = executor.submit(self.process_audio, audio_file)
    #             future.add_done_callback(self.update_answer_with_transcription(answer.id))
    #
    #     return answer
    #
    # def process_audio(self, audio_file):
    #     """
    #     Function to send the audio file to the external API for transcription.
    #     This is executed in a background thread to avoid blocking the main thread.
    #     """
    #     url = f'{settings.BASE_URL}/apis/stt/post/'
    #     files = {'audio': ('tim_original.mp3', audio_file.read(), 'audio/mpeg')}
    #
    #     try:
    #         response = requests.post(url, files=files)
    #         response.raise_for_status()
    #         return response.json().get('transcription', None)
    #     except requests.RequestException as e:
    #         return None  # Return None if transcription fails


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id', 'user', 'summary_audio', 'summary')
