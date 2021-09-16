# **Authentication System** Ⅰ

## The Django Authentication System

- django 인증 시스템은 django.contrib.auth에 django contrib module로 제공된다.
- 필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS 설정에 나열된 아래 두 항목으로 구성된다.
  - `django.contrib.auth`
  - `django.contrib.contenttypes`

### django.contrib.auth

- 인증 프레임워크의 핵심과 기본 모델을 포함한다.

### django.contrib.contenttypes

- 사용자가 생성한 모델과 권한을 연결할 수 있다.



- django 인증 시스템은 **인증(Authentication)**과 **권한(Authorization)** 부여를 함께 제공(처리)하며, 이러한 기능이 어느 정도 결합되어 일반적으로 인증 시스템이라고 한다.

### 인증(Authentication)

- 신원 확인
- 사용자가 자신이 누구인지 확인하는 것

### 권한(Authorization)

- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업을 결정



# 쿠키와 세션

## HTTP

- Hyper Text Transfer Protocol (Secure)
- HTML 문서와 같은 리소스(자원, 데이터)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트 - 서버 프로토콜이기도 하다.



## HTTP 특징

- **`비연결지향 (connectionless)`**
  - **서버는 요청에 대한 응답을 보낸 후 연결을 끊는다.**
- **`무상태 (stateless)`**
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 **상태 정보가 유지되지 않는다**.
  - 클라이언트와 서버가 주고 받은 메세지들은 서로 완전히 독립적이다.
- ***클라이언트와 서버의 지속적인 관계를 유지하기 위해***  `쿠키와 세션`***이 존재한다.***



## 쿠키 (Cookie)

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  - 브라우저(클라이언트)는 쿠키를 로컬에 **KEY-VALUE의 데이터 형식으로 저장**한다.
  - 이렇게 쿠키를 저장해 놓았다가, **동일한 서버에 재요청 시 저장된 쿠키를 함께 전송**한다.

[참고] 소프트웨어가 아니기 때문에 프로그램처럼 실행될 수 없으며 악성코드를 설치 할 수 없지만, 사용자의 행동을 추적하거나 쿠키를 훔쳐서 해당 사용자의 계정 접근 권한을 획득할 수도 있다.

- HTTP 쿠키는 상태가 있는 세션을 만들어 준다.
- 쿠키는 두 요청이 동일한 브라우저에 들어왔는지 아닌지를 판단할 때 주로 사용한다.
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있다.
  - **상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문**이다.

→ ***웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재요청시 요청과 함께 쿠키도 전송한다.***



## 쿠키의 사용 목적

1. 세션 관리 (Session management)
   - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화 (Personalization)
   - 사용자 선호, 테마 등의 설정
3. 트래킹 (Tracking)
   - 사용자 행동을 기록 및 분석



## 세션 (Session)

- 사이트와 특정 브라우저 사이의 **"상태(state)"를 유지시키는 것**
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 발급 받은 session id를 쿠키에 저장
  - 클라이언트가 다시 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
- ID는 세션을 구분하기 위해 필요하며, **쿠키에는 ID만 저장**한다.



## 쿠키 lifetime (수명)

- 쿠키의 수명은 두 가지 방법으로 정의할 수 있다.

1. **`Session cookies`**
   - 현재 세션이 종료되면 삭제된다.
   - 브라우저가 "현재 세션(current session)"이 종료되는 시기를 정의
   - [참고] 일부 브라우저는 다시 시작할 때 세션 복원(session restoring)을 사용해 세션 쿠키가 오래 지속될 수 있도록 한다.
2. **`Persistent cookies(Permanent cookies)`**
   - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제된다.



## Session in Django

- django의 세션은 미들웨어를 통해 구현된다.
- django는 database-backed sessions 저장 방식을 기본 값으로 사용한다.
  - [참고] 설정을 통해 cached, file-based, cookie-based 방식으로 변경 가능하다.
- django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아낸다.
  - 세션 정보는 django db의 **`django_session` 테이블에 저장**된다.
- 모든 것을 세션으로 사용하려고하면, 사용자가 많을 때 서버에 부하가 걸릴 수 있다.
  - 굳이 노출되어도 상관없는 데이터들은 쿠키를 사용해도 무관



## Authentication System in MIDDLEWARE

### SessionMiddleware

- 요청 전반에 걸쳐 세션을 관리

### AutheticationMiddleware

- 세션을 사용하여 사용자를 요청과 연결

### [참고] MIDDLEWARE (미들웨어)

- http 요청과 응답 처리 중간에서 작동하는 시스템(hooks)
- django는 http 요청이 들어오면 미들웨어를 거쳐 해당 URL에 등록되어 있는 view로 연결해주고, http 응답 역시 미들웨어를 거쳐서 내보낸다.
- 주로 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 담당



# 로그인

- 로그인은 Session을 Create하는 로직과 같다.
  - 그러나, User를 Create하는 것이 아니다.
- django는 우리가 session의 메커니즘에 대해 생각하지 않게 도움을 준다.
  - 이를 위해 **인증에 관한 built-in forms를 제공**한다.



## Authentication Form

- 사용자 로그인을 위한 form
- request를 첫번째 인자로 취한다.



## login 함수

### `login(request, user, backend=None)`

```python
from django.contrib.auth import login
```

- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 login()함수가 필요하다.
- 사용자를 로그인시키며 view 함수에서 사용된다.
- HttpRequest 객체와 User 객체가 필요하다.
- django의 session framework를 사용하여 세션에 user의 ID를 저장한다. (→로그인)



### get_user()

- AuthenticationForm의 인스턴스 메서드
- user_cache는 인스턴스 생성 시에 None으로 할당되며, 유효성 검사를 통과했을 경우 로그인한 사용자 객체로 할당된다.
- 인스턴스 유효성을 먼저 확인하고, 인스턴스가 유효할 때만 user를 제공하려는 구조이다.

```python
class AuthenticationForm(forms.Form):
    def get_user(self):
        return self.user_cache
```



# Authentication data in templates

- 현재 로그인 되어있는 유저 정보 출력

  ```html
  <!-- base.html -->
  ...
  <body>
    <div class="container">
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:login' %}">LOGIN</a>
      {% block content %}
      {% endblock content %}
    </div>
    ...
  </body>
  ```

![](images/login.png)



## Authentication data in templates

### context processors

- 템플릿이 렌더링 될 때 자동으로 호출 가능한 context 데이터 목록
- 작성된 프로세서는 RequestContext에서 사용 가능한 변수로 포함된다.

### Users

- 템플릿 RequestContext를 렌더링할 때, 현재 로그인한 사용자를 나타내는 auth.User 인스턴스(또는 클라이언트가 로그인하지 않은 경우 AnonymousUser 인스턴스)는 템플릿 변수 {{ user }}에 저장된다.



# 로그아웃

- 로그인은 Session을 Delete하는 로직과 같다.
  - User를 삭제하는 것이 아니라, 세션을 삭제하는 것이다.



## logout 함수

### `logout(request)`

```python
from django.contrib.auth import logout
```

- HttpRequest 객체를 인자로 받고 반환 값이 없다.
- 사용자가 로그인하지 않은 경우에도 오류를 발생시키지 않는다.
- 현재 요청에 대한 session data를 **DB에서 완전히 삭제**하고, **클라이언트의 쿠키에서도 sessionid가 삭제**된다.
- 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 **사용자의 세션 데이터에 엑세스하는 것을 방지**하기 위함이다.



# 로그인 사용자에 대한 접근 제한

## Limiting access to login-in users

- 로그인 사용자에 대한 엑세스 제한 2가지 방법
  1. The raw way
     - **`is_authenticated` attribute**
  2. The **`login_required` decorator**

### 1. `is_authenticated` attribute

- User model의 속성(attributes) 중 하나
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성 
  - AnonymousUser에 대해서는 항상 False
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 일반적으로 request.user에서 이 속성을 사용하며, 미들웨어의 'django.contrib.auth.middleware.AuthenticationMiddleware'를 통과했는지 확인
- 단, ***권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않는다.***

### 2. `login_required` decorator

- 사용자가 로그인되어 있지 않으면, `settings.LOGIN_URL`에 설정된 문자열 기반 절대 경로로 redirect한다.
  - LOGIN_URL의 기본 값은 `'/accounts/login'`
  - **두번째 app 이름을 accounts로 했던 이유 중 하나이다.**
- 사용자가 로그인되어 있으면 정상적으로 view 함수를 실행
- 인증 성공 시 사용자가 redirect 되어야하는 경로는 `"next"`라는 쿼리 문자열 매개변수에 저장된다.
  - /accounts/login/?`next=/articles/create`

```python
from django.contrib.auth.decorators import login_required
```

### "next" query string parameter

- 로그인이 정상적으로 진행되면 기존에 요청했던 주소로 redirect 하기 위해 마치 주소를 keep 해주는 것
- 단, 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게 된다.

### 두 데코레이터로 인해 발생하는 구조적 문제와 해결

- `@require_POST` 작성된 함수에 `@login_required`를 함께 사용하는 경우 에러가 발생한다.
- 로그인 이후 "next"매개변수를 따라 해당 함수로 다시 redirect 되는데, 이 때 `@require_POST` 때문에 405 에러가 발생하게 된다.
- 두 가지 문제 발생
  1. redirect 과정에서 POST 데이터의 손실
  2. redirect 요청은 POST 방식이 불가능하기 때문에 GET 방식으로 요청된다.
- 문제의 해결
  - 두 데코레이터 중 하나를 변경해준다!!
  - **`@login_required`**는 **GET method request를 처리할 수 있는** view 함수에서만 사용해야 한다.