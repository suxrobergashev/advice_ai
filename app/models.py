from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),)


class Users(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(default=6)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number


class Questions(models.Model):
    age = models.IntegerField(default=6)
    question = models.TextField()
    question_audio = models.FileField(upload_to='questions/audio')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question[:10]


class Answer(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.TextField()
    answer_audio = models.FileField(upload_to='answers/audio')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer[:10]


class Summary(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    summary = models.TextField()
    summary_audio = models.FileField(upload_to='summaries/audio')


class Chat(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ManyToManyField(Questions, blank=True)
    answer = models.ManyToManyField(Answer, blank=True)
    question_count = models.IntegerField(default=0)
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name
