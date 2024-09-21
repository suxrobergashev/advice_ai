from .models import Users, Questions, Answer, Chat, Summary
from rest_framework import serializers
import requests


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

            # Process audio asynchronously
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self.process_audio, audio_file)
                future.add_done_callback(self.update_answer_with_transcription(validated_data))

        # If 'answer' is already provided, it will be used as is
        return super().create(validated_data)

    def process_audio(self, audio_file):
        """
        Function to send the audio file to the external API for transcription.
        This is executed in a background thread to avoid blocking the main thread.
        """
        url = 'https://1bb5-94-158-59-178.ngrok-free.app/apis/stt/post/'
        files = {'audio': ('tim_original.mp3', audio_file.read(), 'audio/mpeg')}

        try:
            response = requests.post(url, files=files)
            response.raise_for_status()
            return response.json().get('transcription', None)
        except requests.RequestException as e:
            return None  # Return None if transcription fails

    def update_answer_with_transcription(self, validated_data):
        """
        Callback function to update the `answer` field with the transcription
        once the audio processing is complete.
        """

        def callback(future):
            transcription = future.result()
            if transcription:
                validated_data['answer'] = transcription
            else:
                validated_data['answer'] = 'Failed to process audio'
            self.save_answer(validated_data)

        return callback

    def save_answer(self, validated_data):
        """
        Save the validated answer data after transcription is completed.
        """
        Answer.objects.create(**validated_data)


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id', 'user', 'summary_audio', 'summary')
