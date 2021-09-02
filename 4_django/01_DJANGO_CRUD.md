# CRUD

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말이다.



## CREATE 

### save() method

- Saving objects
- 객체를 데이터베이스에 저장한다.
- 데이터 생성 시 save()를 호출하기 전에는 **객체의 ID 값이 무엇인지 알 수 없다.** -> ID 값은 django가 아니라 DB에서 계산되기 때문
- 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 **반드시 save()가 필요**

### str method

- 표준 파이썬 클래스의 메소드인 str()을 정의하여, 각각의 object가 사람이 읽을 수 있는 문자열을 반환(return)하도록 할 수 있다.
- **작성 후 반드시 shell_plus 재시작**

```bash
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

```python
# models.py
def __str__(self):
	return self.title
```

```bash
>>> Article.objects.all()
<QuerySet [<Article: first>, <Article: second>, <Article: third>]>
```



### [실습] CREATE 1

- 인스턴스 생성 후 인스턴스 변수 설정

```bash
>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'django!'
>>> Article.objects.all()
<QuerySet[]>
# 최종적으로 save해야 DB에 추가된다.
>>> article.save()
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>]>
```

```bash
# 조회할 때 참고 사항
# 테이블 column은 id라고 저장되어 있고, 둘 다 같은 값을 내보내지만
# django는 pk를 사용할 것을 권장
>>> article.id
1
>>> article.pk
1
#######################################################################
In [10]: article.created_at
Out[10]: datetime.datetime(2021, 9, 1, 6, 28, 33, 994380, tzinfo=<UTC>)
```

### [실습] CREATE 2

- 초기 값과 함께 인스턴스 생성

```bash
>>> article = Article(title='second', content='django!!')
>>> article
<Article: Article object (None)>
# 최종적으로 save해야 DB에 추가된다.
>>> article.save()
>>> article
<Article: Article object (2)>
```

### [실습] CREATE 3

- QuerySet API - create() 사용

```bash
# save를 안해도 DB에 추가된다.
>>> Article.objects.create(title='third', content='django!!!')
<Article: Article object (3)>
```





## READ

- QuerySet API method를 사용해 다양한 조회를 하는 것이 중요
- QuerySet API method는 크게 2가지로 분류
  - Methods that **return new querysets**
  - Methods that **do not return querysets**



### all()

- 현재 QuerySet의 복사본을 반환

```bash
>>> Article.objects.all()
<QuerySet [<Article: first>, <Article: second>, <Article: third>]>
```

### get()

- 주어진 lookup 매개변수와 일치하는 객체를 반환 (객체 하나)
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생시킨다.
- 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 **고유성(unique)을 보장하는 조회**에서 사용해야 한다.

```bash
>>> article = Article.objects.get(pk=100)
DoesNotExist: Article matching query does not exist.
>>> Article.objects.get(content='django!')
<Article: first>
```

### filter()

- 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

```bash
>>> Article.objects.filter(content='django!!')
<QuerySet [<Article: second>]>
# 없는 값을 조회해도 오류가 발생하지 않는다.
>>> Article.objects.filter(title='forth')
<QuerySet []>
```



### [실습] READ

```bash
# DB에 인스턴스 객체를 얻기 위한 쿼리문 날리기
# 이때, 레코드가 하나만 있으면 인스턴스 객체로, 두 개 이상이면 쿼리셋으로 리턴

# 전체 article 객체 조회
>>> Article.objects.all()
<QuerySet[]>
```





## UPDATE



### [실습] UPDATE

```bash
# 수정할 객체 선택
>>> article = Article.objects.get(pk=1)
>>> article
<Article: first>
>>> article.title = 'byebye'
>>> article.save()
>>> article.title
'byebye'
```





## DELETE

- QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환
- 삭제된 것을 재사용하지 않기 때문에, pk=1(id=1)인 것을 삭제한 뒤 다른 것을 추가해도 pk=1(id=1)에 저장되는 것이 아니라 다음 id로 추가된다.



### [실습] DELETE

```bash
# 삭제할 객체 선택
>>> article = Article.objects.get(pk=1)
>>> article
<Article: byebye>
# 삭제의 반환 값이 있다.
>>> article.delete()
(1, {'articles.Article': 1})
>>> Article.objects.all()
<QuerySet [<Article: second>, <Article: third>]>
```



# CRUD with views

## HTTP method

### GET

- 특정 리소스를 **가져오도록 요청할 때 사용**
- 반드시 데이터를 가져올 때만 사용해야 한다.
- DB에 변화를 주지 않는다. -> 검색 결과를 단순히 조회
- CRUD에서 R 역할을 담당



### POST

- 서버로 데이터를 **전송할 때 사용**
- 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
- 서버에 변경사항을 만든다.
- CRUD에서 C, U, D 역할을 담당



## 사이트 간 요청 위조 (CSRF, Cross Site Request Forgert)

- 웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- django는 CSRF에 대항하여 middleware와 template tag를 제공한다.

## CSRF 공격 방어

- Security Token 사용 방식 (CSRF Token)
  - 사용자의 데이터에 **임의의 난수 값을 부여**해 매 요청마다 해당 **난수 값을 포함시켜 전송** 시키도록 한다.
  - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증후 저장
- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용 (GET제외)
- django는 csrf token 템플릿 태그를 제공

### csrf_token template tag

```django
{% csrf_token %}
```

- CSRF 보호에 사용
- input type이 hidden으로 작성되며 value는 django에서 생성한 hash 값으로 설정된다.
- 해당 태그 없이 요청을 보낸다면 django 서버는 403 forbidden을 응답
