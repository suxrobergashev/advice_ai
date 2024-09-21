from .models import Chat, Questions


def get_active_chat(user):
    return Chat.objects.filter(user=user, is_closed=False).first()


def get_random_question(exclude_ids):
    return Questions.objects.exclude(id__in=exclude_ids).order_by('?').first()
