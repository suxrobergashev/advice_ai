from django.contrib import admin
from .models import Users, Answer, Questions, Chat, Summary


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'age', 'gender', 'phone_number')
    search_fields = ('full_name', 'age', 'gender', 'phone_number')
    list_filter = ('age', 'gender', 'phone_number')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')