from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class Question(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.TextField()


    def __str__(self):
        return self.question
    


class Answer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.TextField()


    def __str__(self):
        return self.answer