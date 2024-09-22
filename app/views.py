from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import Users, Chat, Questions
from .serializers import UserSerializer, LoginSerializer, TokenSerializer, QuestionSerializer, AnswerSerializer
from .utils import get_active_chat, get_random_question


class RegisterView(ViewSet):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: 'User created successfully'}
    )
    def create(self, request):
        user = Users.objects.filter(phone_number=request.data['phone_number']).exists()
        if user:
            raise CustomApiException(ErrorCodes.ALREADY_EXISTS)
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response({'result': 'User created successfully ', 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: TokenSerializer()}
    )
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        user = Users.objects.filter(phone_number=request.data['phone_number']).first()
        if not user:
            raise CustomApiException(ErrorCodes.USER_DOES_NOT_EXIST)
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        return Response(
            data={'result': {'access_token': str(access_token), 'refresh_token': str(refresh)},
                  'ok': True},
            status=status.HTTP_200_OK)


class QuestionViewSet(ViewSet):
    @swagger_auto_schema(
        responses={201: QuestionSerializer()},
    )
    def create_chat(self, request):
        user = request.user

        chat = get_active_chat(user)
        if chat:
            chat.question.clear()
            chat.answer.clear()
            # Reset question count
            chat.question_count = 0
            chat.save()

        else:
            chat = Chat.objects.create(user=user)
        chat.save()
        question = get_random_question([])
        chat.question.add(question)
        chat.question_count = 1
        chat.save()

        return Response(
            {'result': QuestionSerializer(question, context={'request': request}).data, 'chat': chat.id, 'ok': True},
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        responses={200: QuestionSerializer()}
    )
    def next_question(self, request, pk):
        chat = Chat.objects.filter(user=request.user, is_closed=False, id=pk).first()
        if not chat:
            raise CustomApiException(ErrorCodes.NOT_FOUND)

        question = get_random_question(chat.question.values_list('id', flat=True))
        chat.question.add(question)
        chat.question_count += 1
        chat.save()

        end_game = chat.question_count == 5
        return Response(
            {'result': QuestionSerializer(question, context={'request': request}).data, 'chat': chat.id,
             'end': end_game, 'ok': True},
            status=status.HTTP_200_OK
        )


class AnswerViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=AnswerSerializer,
        responses={200: AnswerSerializer()}
    )
    def create(self, request, pk):
        chat = get_active_chat(request.user)
        if not chat:
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='Chat does not exist')
        if pk not in chat.question.values_list('id', flat=True):
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='Question does not exist')
        data = request.data.copy()
        data.update({'user': request.user.id, 'question': pk})

        # If 'answer_audio' is provided but 'answer' is not, add a placeholder
        serializer = AnswerSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        answer_instance = serializer.save()

        # Add the actual Answer instance to the chat, not the serialized data
        chat.answer.add(answer_instance)
        chat.save()

        return Response({'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class Summary(ViewSet):
    @swagger_auto_schema(
        responses={}
    )
    def create(self, request, pk):
        chat = get_active_chat(request.user)
        if not chat:
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='Chat does not exist')
        pass
