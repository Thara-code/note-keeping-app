from django.db import models

# Create your models here.

class Note(models.Model):
  note_title = models.CharField(max_length=30)
  note_desc = models.TextField()
  #time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.note_title