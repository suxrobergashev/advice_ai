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



def get_active_chat(user):
    """
    Retrieves the active chat for the user. Returns None if no active chat exists.

    :param user: The user for whom the chat is retrieved.
    :return: The active Chat object or None.
    """
    return Chat.objects.filter(user=user, is_closed=False).first()

#
# def send_chat_for_analysis(user, chat_id):
#     """
#     Sends chat questions and answers to an external API for processing and retrieves a response.
#
#     :param user: The user object.
#     :param chat_id: The chat ID to retrieve questions and answers.
#     :return: The response text from the external API.
#     """
#     # Retrieve the chat object
#     chat = Chat.objects.filter(user=user, is_closed=False, id=chat_id).first()
#     if not chat:
#         raise CustomApiException(ErrorCodes.NOT_FOUND)
#
#     # Extract questions and answers
#     questions = chat.question.values_list("question", flat=True)
#     answers = chat.answer.values_list("answer", flat=True)
#
#     # Prepare content for the API based on questions and answers
#     messages = []
#     for question, answer in zip(questions, answers):
#         messages.append({
#             "role": "user",
#             "content": f"Savol: {question}\nJavob: {answer}"
#         })
#
#     # Define the API URL and headers
#     url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"
#     headers = {
#         "x-rapidapi-key": "22bbcfaf16msh6ff33c352478181p1d164djsn67b305c8fc5d",
#         "x-rapidapi-host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com",
#         "Content-Type": "application/json"
#     }
#
#     # Prepare the API payload
#     payload = {
#         "messages": messages,
#         "model": "gpt-4o",
#         "system_prompt": "Vazifangiz berilgan savol va javoblar asosida foydalanuvchining kasbini bashorat qilishdir. Javoblarda kasb bilan bog'liq bo'lishi mumkin bo'lgan vazifalar, ko'nikmalar yoki boshqa elementlarni tahlil qiling va foydalanuvchining qaysi kasbga mansubligini aniqlang. Agar javoblar noaniq yoki kasbni aniqlash uchun yetarli ma'lumot bermasa, 'Kasbni aniqlash uchun yetarli ma'lumot mavjud emas' deb javob bering.",
#         "max_tokens": 500,
#         "temperature": 0.5
#     }
#
#     # Send the request to the external API
#     response = requests.post(url, json=payload, headers=headers)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         result = response.json()
#
#         # Extract the response content
#         response_text = result.get("choices", [{}])[0].get("message", {}).get("content", "")
#
#         # If there's a valid response, return the text
#         if response_text:
#             return response_text
#         else:
#             return "There was a problem analyzing the chat."
#     else:
#         raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='Failed to connect to the external API.')
#


def save_summary_audio(user, transcript, summary_text, chat):
    """
    Sends the transcript to the TTS API, saves the audio file, and saves the file path to the model.

    :param user: The user for whom the summary is created.
    :param transcript: The text to be converted into audio.
    :param summary_text: The summary text to save.
    :return: The created Summary object.
    """
    # TTS API URL
    url = f"{settings.BASE_URL}apis/tts/post/"

    # Payload for the POST request
    payload = {'transcript': transcript}

    # Make the request to the TTS API
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        # Define a path to save the audio file
        audio_filename = f"{user.id}_output_audio.mp3"
        audio_path = os.path.join("summaries/audio", audio_filename)  # Save relative path

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)

        # Save the audio response to a file
        with open(audio_path, "wb") as audio_file:
            audio_file.write(response.content)

        # Create a new Summary object and save only the audio file path
        summary_instance = Summary(
            chat_id=chat.id,
            user=user,
            summary=summary_text,
            summary_audio=audio_path  # Saving the file path
        )
        summary_instance.save()

        print(f"Audio saved at: {audio_path}")
        return summary_instance
    else:
        raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='There was a problem connecting to the TTS API.')