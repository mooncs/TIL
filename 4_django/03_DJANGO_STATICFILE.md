# Static files

## Static files

- 정적 파일
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 (움직이지 않는) 추가 파일을 제공해야 한다.
- django에서는 이러한 파일들을 "**static file**"이라고 한다.



## Static file의 구성

1. **`django.contrib.staticfiles`**가 INSTALLED_APPS에 포함되어 있는지 확인한다.

2. settings.py에서 **STATIC_URL**을 정의한다.

3. 템플릿에서 **`static 템플릿 태그`**를 사용하여 지정된 상대경로에 대한 URL을 빌드한다.

   ```django
   {% load static %}
   
   <img src="{% static 'my_app/example.jpg' %}" alt="My image">
   ```

4. 앱의 static 폴더에 정적 파일을 저장한다. (→ templates와 유사한 경로)



## django template tag

### load

- 사용자 정의 템플릿 태그 세트를 로드
- 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드

### static

- STATIC_ROOT에 저장된 정적 파일에 연결



## The staticfiles app

### STATIC_ROOT

- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
- django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
- 개발과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않는다.
  - 직접 작성하지 않으면 django 프로젝트에서는 settings.py에 작성되어 있지 않다.
- 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함이다.



### [참고] collectstatic

- STATIC_ROOT에 정적 파일을 수집

```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

```bash
$ python manage.py collectstatic
```



### STATIC_URL

- STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
  - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색한다.
  - **실제 파일이나 디렉토리가 아니며, URL로만 존재**
  - 비어 있지 않은 값으로 설정한다면 **반드시 "`/`"로 끝나야 한다.**



### STATICFILES_DIRS

- app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포한하는 문자열 목록으로 작성되어야 한다.



## 정적 파일 사용하기

### 1-1. 정적 파일 경로

app_name/static/app_name

### 1-2. template에서 경로 참조

```django
{# app_name/detail.html #}
{% extends 'base.html' %}
{% load static %}

{% block content %}
  {# 명시적으로 구분하기 위해서 app_name/사용 #}
	<img src="{% static 'app_name/image_name.jpg'%}" alt="sample">
	...
{% endblock content %}
```



### 2-1. 정적 파일 위치 및 추가 경로 작성

static/images

```python
# settings.py
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### 2-2. template에서 경로 참조

```django
{# base.html #}
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  ...
</head>
<body>
  <img src="{% static 'images/image_name.jpg'%}" alt="sample">
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
</body>
</html>
```



# 이미지 업로드(기본 설정)

## Media file

- 미디어 파일
- 사용자가 웹에서 업로드하는 정적 파일
- 유저가 업로드 한 모든 정적 파일



## ImageField

- 이미지 업로드에 사용되는 모델 필드
- **FileField를 상속받는 서브 클래스**이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며, 
- 더해서 사용자에 의해 업로드 된 객체가 **유효한 이미지인지 검사**한다.
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있다.
  - **이미지 파일의 경로**가 문자열로 저장된다.
- [주의] 사용하려면 반드시 `Pillow` 라이브러리가 필요하다.



## FileField

- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 가지고 있다.
  1. upload_to
  2. storage

### upload_to

- 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법을 제공

  1. 문자열 값이나 경로 지정

     - 파이썬의 strftime() 형식이 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체된다.

     ```python
     # models.py
     class MyModel(modles.Model):
         # 1. MEDIA_ROOT/uploads/ 경로로 파일 업로드
         upload = models.FileField(upload_to='uploads/')
         # 2. MEDIA_ROOT/uploads/2021/01/01 경로로 파일 업로드( strftime() )
         upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
     ```

  2. 함수 호출

     - **반드시 2개의 인자(`instance`, `filename`)를 사용**한다.

     1. **instance**
        - FileField가 정의된 모델의 인스턴스
        - 대부분의 이 객체는 아직 데이터베이스에 저장되지 않았으므로 PK값이 아직 없을 수 있다.
     2. **filename**
        - 기존 파일에 제공된 파일 이름

     ```python
     # models.py
     
     def articles_image_path(instance, filename):
         # MEDIA_ROOT/user_<pk>/ 경로로, <filename> 이름으로 업로드
         return f'user_{instance.user.pk}/{filename}'
     
     class Article(models.Model):
         image = models.ImageField(upload_to=articles_image_path)
     ```



### ImageField를 사용하기 위한 몇 가지 단계

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

2. upload_to  속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정

3. 업로드 된 파일의 경로는 django가 제공하는 'url' 속성을 통해 얻을 수 있다.

   ```django
   <img src="{{ articles.image.url }}" alt="{{ article.image }}">
   ```

4. Pillow 라이브러리 설치 필요

   ```bash
   $ pip install Pillow
   
   $ python manage.py makemigrations
   $ python manage.py migrate
   
   $ pip freeze > requirements.txt
   ```



## MEDIA_ROOT

- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
- django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않는다.
  - 실제 데이터베이스에 저장되는 것은 **파일의 경로**
- [주의] MEDIA_ROOT는 **STATIC_ROOT와 반드시 다른 경로로 지정해야 한다.**

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
```



## MEDIA_URL

- MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
- 업로드 된 파일의 주소를 만들어주는 역할을 한다.
  - 웹 서버 사용자가 사용하는 public URL
- 비어 있지 않은 값으로 설정한다면 **반드시 "`/`"로 끝나야 한다.**
- [주의] MEDIA_URL은 **STATIC_URL과 반드시 다른 경로로 지정해야 한다.**

```python
# settings.py
MEDIA_URL = '/media/'
```



## 개발 단계에서 사용자가 업로드한 파일 제공하기

```python
# crud/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# MEDIA_URL과 MEDIA_ROOT가 미리 작성되어 있어야 한다.
# 업로드 된 파일의 URL == settings.MEDIA_URL
# 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
```

사용자가 업로드한 파일이 우리 프로젝트에 업로드 되지만, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요하다.

[참고] https://docs.djangoproject.com/ko/3.2/howto/static-files/



## STATIC_URL과 MEDIA_URL

- static과 media 결국 모두 서버에 요청해서 조회하는 것이다.
- 서버에 요청하기 위한 url을 urls.py가 아닌 settings에 먼저 작성 후 urlpatterns에 추가하는 형식



# 이미지 업로드(CREATE)

## ImageField 작성

### upload_to='images/'

- 실제 이미지가 저장되는 경로를 지정

### blank=True

- 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정 (이미지를 선택적으로 업로드 할 수 있도록)

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # save to 'MEDIA_ROOT/images'
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



## Model field option - "blank"

- 기본 값 : False
- True인 경우 필드를 비워 둘 수 있다.
  - DB에는 빈 문자열이 저장된다.
- 유효성 검사에서 사용된다.(is_vaild)
  - 필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있다.



## Model field option - "null"

- 기본 값 : False
- True인 경우 django는 빈 값을 DB에 NULL로 저장한다.
- 주의사항
  - CharField, TextField와 같은 **문자열 기반 필드에는 사용하는 것을 피해야 한다.**
  - 문자열 기반 필드에 True로 설정시, '데이터 없음(no data)'에 1. "빈 문자열", 2. "NULL"의 2가지 가능한 값이 존재하게 된다.
  - 대부분의 경우 "데이터 없음"에 대해 두 개의 가능한 값을 갖는 것은 중복된다.
  - django는 NULL이 아닌 빈 문자열을 사용하는 것이 규칙이다. 



## blank vs null

### blank

- Validation-related, 유효성 검사 관련

### null

- Database-related, DB관련

문자열 기반 및 비문자열 기반 필드 모두에 대해 **null option은 DB에만 영향**을 미치므로,

**form**에서 빈 값을 허용하려면 **blank=True**를 설정해야한다.



## [참고] 게시글 작성 form enctype 속성 지정

```django
{# articles/templates/articles/create.html #}
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
```

## form 요소 - enctype(인코딩) 속성

### 1. multipart/form-data

- 파일 /이미지 업로드 시에 반드시 사용해야 한다. (전송되는 데이터의 형식을 지정)
- \<input type="file">을 사용할 경우에 사용

### 2. application/x-www-form-urlencoded

- (기본값) 모든 문자 인코딩

### 3. text/plain

- 인코딩을 하지 않은 문자 상태로 전송
- 공백은 '+' 기호로 변환하지만, 특수 문자는 인코딩 하지 않는다.



\* 참고 : **동일명의 이미지를 업로드**하여도 임의의 난수를 파일명에 붙여서 저장되기에 아무런 문제가 되지 않는다.



# 이미지 업로드(READ)

## 이미지 경로 불러오기

- **`article.image.url`** == 업로드 파일의 경로
- **`article.image`** == 업로드 파일의 파일 이름

```django
{# articles/templates/articles/detail.html #}
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```



## STATIC_URL & MEDIA_URL

- static, media 모두 서버에 요청해서 조회하는 것이다.
- 서버에 요청하기 위한 url을 urls.py가 아닌 settings.py에 먼저 작성 후 urlpatterns에 추가하는 형식



# 이미지 업로드(UPDATE)

## 이미지 수정하기

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정하는 것은 불가능하다.
- 때문에 새로운 사진으로 덮어 씌우는 방식을 사용한다.

```django
{# articles/templates/articles/update.html #}
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
```

```python
# articles/views.py
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        # form = ArticleForm(data=request.POST, files=request.FILES, instance=article)
```

- 이미지가 없어 출력 못하는 경우 해결

```django
{# articles/templates/articles/detail.html #}
{% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
{% else %}
	<img src="{% static 'images/default.jpg' %}" alt="default image"> 
{% endif %}
```



# 이미지 Resizing

## 이미지 크기 변경하기

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 자업
- \<img>태그에서 직접 사이즈를 조정할 수도 있지만(width&height), 업로드 될 때 이미지 자체를 resizing하는 것을 사용
- **`django-imagekit`** 라이브러리 활용

```bash
$ pip install django-imagekit

$ pip freeze > requirements.txt
```

```python
# settings.py
INSTALLED_APP = [
    ...,
    'imagekit',
    ...,
]
```

- 원본 이미지를 재가공하여 저장(원본x, 썸네일o)

```python
# models.py
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

# 원본을 저장하지 않고, resize된 사진을 저장 → 원본을 유지하지 않는다.
image = ProcessedImageField(
	upload_to='thumbnails/',
	processors=[ResizeToFill(100, 50)],
	format='JPEG',
	options={'quality': 60},
)
# 원본을 유지
image = models.ImageField(upload_to='origins/', blank=True)
image_thumbnail = ImageSpecField(
    source='image',
    processors=[ResizeToFill(100, 50)],
    format='JPEG',
    options={'quality': 90},
)
```

```django
{# articles/templates/articles/detail.html #}
{# 이미지 resize하기 #}
{% if article.image %}
<img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
{% else %}
<img src="{% static 'images/default.jpg' %}" alt="default image">
{% endif %}
```



