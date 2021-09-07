# django Form Class

## Intro

- 우리는 지금까지 HTML form, input을 통해서 사용자로부터 데이터를 받았다.
- 이렇게 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시하며, 유효한 데이터에 대해 요구되는 동작을 수행하는 것을 "**올바르게 하기**" 위해서는 꽤나 많은 노력이 필요하다.
- django는 일부 과중한 작업과 반복 코드를 줄여줌으로써, 이 작업을 훨씬 쉽게 만들어 준다. → "**django Form**"



## django's forms

- Form은 django 프로젝트의 주요 유효성 검사 도구들 중 하나이며, 공격 및 우연한 데이터 손상에 대한 중요한 **방어수단**이다.
- django는 위와 같은 Form 기능의 방대한 부분을 단순화하고 자동화 할 수 있으며, 프로그래머가 직접 작성한 코드에서 수행할 수 있는 것보다 더 안전하게 수행할 수 있다.
- django가 제공하는 Form에 관련된 작업 세 가지 (렌더링부터 처리까지)
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML Forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리



## The django "Form Class"

- django Form 관리 시스템의 핵심
- Form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러 메세지를 결정
- django는 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여준다.



## Form 선언하기

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- Model을 선언하는 것과 유사하며 같은 필드타입을 사용(또한, 일부 매개변수도 유사하다.)
- forms 라이브러리에서 파생된 Form 클래스를 상속받는다.



## Form rendering options

- \<label> & \<input> 쌍에 대한 3가지 출력 옵션

  1. as_p()

     - 각 필드가 단락(\<p> 태그)으로 감싸져서 렌더링 된다.

     ```django
     {{ form.as_p }}
     ```

  2. as_ul()

     - 각 필드가 목록 항목(\<li> 태그)으로 감싸져서 렌더링 된다.
     - \<ul> 태그는 직접 작성해야 한다.

  3. as_table()

     - 각 필드가 테이블(\<tr> 태그)행으로 감싸져서 렌더링 된다.
     - \<table>태그는 직접 작성해야 한다.



## django의 HTML input 요소 표현 방법 2가지

1. **Form fields**
   - input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용된다.
2. **Widgets**
   - 웹 페이지의 HTML input 요소 렌더링
   - GET/POST 딕셔너리에서 데이터 추출
   - 하지만 **widgets은 반드시 form fields에 할당 된다.**

```python
title = forms.CharField(max_length=10)
content = forms.CharField(widget=forms.Textarea)
```



## Widgets

- django의 HTML input element 표현
- HTML 렌더링을 처리
- 주의 사항
  - Form Fields와 혼동되어서는 안된다.
  - Form Fields는 ipnut 유효성 검사를 처리
  - Widgets은 웹페이지에서 input element의 **단순 raw한 렌더링 처리**

* 참고 https://docs.djangoproject.com/en/3.2/ref/forms/widgets/#textarea



# ModelForm

## Intro

- 모델이 있고 사용자가 게시글을 제출할 수 있는 양식을 만들고 싶은 경우 이미 모델에서 필드를 정의했기 때문에 form에서 필드를 재정의하는 중복된 행위가 발생한다.
- 그래서 django는 Model을 통해 Form Class를 만들 수 있는 Helper를 제공한다. → "**Model Form**"



## ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 Helper
- 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능하다.



## ModelForm 선언하기

```python
# articles/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 필드를 재정의하지 않는다.
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받는다.
- 정의한 클래스 안에 Meta 클래스를 선언하고, 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta클래스에 지정한다.



## Meta class

- **Model의 정보를 작성**하는 곳

- ModelForm을 사용할 경우 사용할 모델이 있어야 하는데 Meta 클래스가 이를 구성한다.

  - 해당 Model에 정의한 field 정보를 Form에 적용하기 위함이다.

- [참고] Inner Class (Nested Class)

  - 클래스 내에 선언된 다른 클래스
  - 관련 클래스를 함께 그룹화하여 가독성 및 프로그램 유지 관리를 지원(논리적으로 묶어서 표현)
  - 외부에서 내부 클래스에 접근할 수 없으므로 코드의 복잡성을 줄일 수 있다.

- [참고] Meta 데이터

  - 데이터에 대한 데이터

    ex> 사진 촬영 - 사진 데이터 - 사진의 메타 데이터(촬영 시각, 렌즈, 조리개 값 등)



## is_vaild() method

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 django는 is_vaild()를 제공

### 	[참고] 유효성 검사

		- 요청한 데이터가 특정 조건에 충족하는지 확인하는지 작업
		- 데이터베이스 각 필드 조건에 올바르지 않은 데이터가 서버로 전송되거나, 저장되지 않도록 하는 것



## save() method

- Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고(반환값이 존재) 저장

- ModelForm의 하위(sub) 클래스는 기존 모델 인스턴스를 키워드 인자 **instance**로 받아들일 수 있다.

  - 이것이 제공되면 save()는 해당 인스턴스를 업데이트 (UPDATE)
  - 제공되지 않는 경우 save()는 지정된 모델의 새 인스턴스를 생성(CREATE)

- Form의 유효성이 확인되지 않은 경우, save를 호출하면 form.errors를 확인하여 에러 확인 가능

  ```python
  # Create a form instance from POST data.
  form = ArticleForm(request.POST)
  
  # CREATE
  # Save a new Article object from the form's data.
  new_article = f.save()
  
  # UPDATE
  # Create a form to edit an existing Article, but use POST data to populate the form.
  article = Article.objects.get(pk=1)
  form = ArticleForm(request.POST, instance=article)
  form.save()
  ```

  

## Widgets 적용하기

- django의 HTML input element 표현
- HTML 렌더링을 처리
- 2가지 작성 방식을 가진다.



### 1. Meta 클래스에 작성

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widget = {
            'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': 'Enter the title',
                'maxlength':10,
            }
          )
        }
```

### 2. 권장

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
	title = forms.CharField(
    	label = '제목',
        widget = forms.TextInput(
        	attrs={
                'class': 'mt-title',
                'placeholder': 'Enter the title',
            }
        ),
    )    
    
    class Meta:
        model = Article
        fields = '__all__'
```



# Form & ModelForm

## Form

- 어떤 model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성
- cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야 한다.
- **model에 연관되지 않은 데이터를 받을 때 사용**한다.

## ModelForm

- django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
- 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save()호출 가능



# Handling HTTP requests

## django에서 HTTP요청을 처리하는 방법

1. **django shortcut functions**
2. **View decorators**



## 1. django shortcut functions

- django.shortcuts 패키지는 개발에 도움 될 수 있는 여러 함수와 클래스를 제공
- shortcuts function 종류
  - render()
  - redirect()
  - get_object_or_404()
  - get_list_or_404()



### get_object_or_404()

- 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 경우 **DoesNotExist** 예외 대신 **Http 404**를 raise

  → 더 정확한 이유를 알려주기 위해서

- get() 메서드의 경우 조건에 맞는 데이터가 없을 경우에 에러를 발생시킨다.

  - 코드 실행 단계에서 발생한 에러게 대해서 브라우저는 **http status code 500으로 인식**한다.

- 상황에 따라 적절한 예외처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 개발의 중요한 요소 중 하나다.



## 2. View decorators

- django는 다양한 HTTP 기능을 지원하기 위해 view에 적용할 수있는 여러 데코레이터를 제공한다.

  **[참고] Decorator(데코레이터)**

  - 어떤 함수에 기능을 추가하고 싶을 때, **해당 함수를 수정하지 않고** 기능을 연장 해주는 함수
  - django는 다양한 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공한다.

- **Allowed HTTP methods**
  - 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
  - 요청이 조건을 충족시키지 못하면 **HttpResponseNotAllowed**를  return (405 Method Not Allowed)
  - **require_http_methods(), require_POST()**, require_safe(), require_GET()



### require_http_methods()

- view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터



### require_POST()

- view 함수가 POST method 요청만 승인하도록 하는 데코레이터

\* 참고 : https://docs.djangoproject.com/en/3.2/topics/http/decorators/







