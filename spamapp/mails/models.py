from django.db import models

# Create your models here.

class mails(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date=models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_spam =models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"