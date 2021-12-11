from django.db import models

# Create your models here.


class FormData(models.Model):
    Question = models.CharField(max_length=150, null=True)
    Clue = models.CharField(max_length=150, null=True)
    Solution = models.CharField(max_length=150, null=True)
    Answer = models.CharField(max_length=150, null=True)
    CorrectAnswer = models.CharField(max_length=150, null=True)
    ImageData = models.ImageField(upload_to='images', default='images/default.jpg')

    class Meta():
        db_table = 'form_data'
