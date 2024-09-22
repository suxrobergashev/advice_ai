from rest_framework import routers
from .views import RegisterView, QuestionViewSet, AnswerViewSet, SummaryViewSet

router = routers.DefaultRouter()
from django.urls import path

urlpatterns = [
    path('authe/register/', RegisterView.as_view({'post': 'create'}), name='register'),
    path('authe/login/', RegisterView.as_view({'post': 'login'}), name='login'),
    path('questions/', QuestionViewSet.as_view({'get': 'create_chat'}), name='questions'),
    path('questions/next/<int:pk>/', QuestionViewSet.as_view({'get': 'next_question'}), name='next_question'),
    path('answer/<int:pk>/', AnswerViewSet.as_view({'post': 'create'}), name='answers'),
    path('summary/', SummaryViewSet.as_view({'get': 'create'}), name='summary'),
]

urlpatterns += router.urls
