from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=1000)
    pub_at = models.DateTimeField('publish date')
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return "{} {} {}".format(self.id, self.text, self.pub_at)

    def was_published_recently(self):
        return self.pub_at >= timezone.now() - datetime.timedelta(days=1)
    pass


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}: {}".format(self.question.id, self.text, self.votes)
    pass
