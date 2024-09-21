from rest_framework_simplejwt.authentication import JWTAuthentication
from exceptions.exception import CustomApiException
from exceptions.error_messages import ErrorCodes
from .models import Users


class CustomJWTAuthentication(JWTAuthentication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = Users

    def get_user(self, validated_token):
        user_id = validated_token['user_id']
        user = Users.objects.filter(id=user_id).first()
        if not user:
            raise CustomApiException(ErrorCodes.UNAUTHORIZED.value)
        return user
