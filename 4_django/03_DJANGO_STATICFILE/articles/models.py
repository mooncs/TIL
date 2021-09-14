from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

def articles_image_path(instance, filename):
    # MEDIA_ROOT/user_<pk>/ 경로로, <filename> 이름으로 업로드
    # 경로 만들기
    return f'user_{instance.user.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    # image = models.ImageField(upload_to='%Y/%m.%d/', blank=True)
    # image = models.ImageField(upload_to=articles_image_path)
    # # 원본을 저장하지 않고, resize된 사진을 저장 → 원본을 유지하지 않는다.
    # image = ProcessedImageField(
    #     upload_to='thumbnails/',
    #     processors=[ResizeToFill(100, 50)],
    #     format='JPEG',
    #     options={'quality': 60},
    # )
    # 원본을 유지
    image = models.ImageField(upload_to='origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
