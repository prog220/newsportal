from django.db import models

# Create your models here.
class New(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    anons = models.CharField(max_length=50)
    text = models.CharField()

    def __str__(self):
        return f"title: {self.title}; anons: {self.anons}; text: {self.text}"