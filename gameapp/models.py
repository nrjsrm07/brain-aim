# models.py

# from djongo import models
from django.db import models

class Questions(models.Model):
    truth_dare = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    question = models.CharField(max_length=255)

    class Meta:
        db_table = 'questions'