from django.db import models

# Create your models here.
class Article(models.Model):
    # CharField, TextField 둘 다 텍스트타입이지만, CharField는 조건이 필요하다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title