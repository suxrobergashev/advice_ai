import os
import requests
from .models import Summary
from django.conf import settings
from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import Questions, Chat

def save_summary_audio(user, transcript, summary_text):
    """
    Sends the transcript to the TTS API, saves the audio file, and saves the file path to the model.

    :param user: The user for whom the summary is created.
    :param transcript: The text to be converted into audio.
    :param summary_text: The summary text to save.
    :return: The created Summary object.
    """
    # TTS API URL
    url = f"{settings.BASE_URL}/apis/tts/post/"

    # Payload for the POST request
    payload = {'transcript': transcript}

    # Make the request to the TTS API
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        # Define a path to save the audio file
        audio_filename = f"{user.id}output_audio.mp3"
        audio_path = os.path.join("summaries/audio", audio_filename)

        # Save the audio response to a file
        with open(audio_path, "wb") as audio_file:
            audio_file.write(response.content)

        # Create a new Summary object and save only the audio file path
        summary_instance = Summary(
            user=user,
            summary=summary_text,
            summary_audio=audio_path  # Saving just the file path
        )
        summary_instance.save()

        print(f"Audio saved at: {audio_path}")
        return summary_instance
    else:
        raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='There was a problem connecting')


def get_active_chat(user):
    return Chat.objects.filter(user=user, is_closed=False).first()

def get_random_question(exclude_ids):
    return Questions.objects.exclude(id__in=exclude_ids).order_by('?').first()