# **Authentication System** Ⅱ

# **회원가입**

## UserCreateForm

- 주어진 username과 password로 **권한이 없는 새 user를 생성**하는 ModelForm
- 3개의 필드를 가진다.
  1. username (from the user model)
  2. password1
  3. password2



# **회원탈퇴**

- 회원탈퇴는 DB에서 사용자를 삭제하는 것과 같다.



# **회원정보수정**

## UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm



## UserChangeForm의 문제점

- admin 인터페이스에서 사용되는 ModelForm이기 때문에 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능해진다.
- 따라서 UserChangeForm을 상속받아 CustomUserChangeForm이라는 서브클래스를 작성해 접근 가능한 필드를 조정해야한다. → accounts/forms.py



## CustomUserChangeForm 작성

1. get_user_model()
2. User 모델의 fields

```python
# accounts/forms.py
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ()
```

### get_user_model()

- 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환한다.

- django는 User 클래스를 직접 참조하는 대신, 

  `django.contrib.auth.get_user_model()`을 사용하여 참조해야 한다고 강조한다.



## User 클래스 상속 구조 살펴보기

1. **`UserChangeForm`** 클래스 구조 확인
   - Meta 클래스를 보면 User라는 model을 참조하는 ModelForm이라는 것을 확인할 수 있다.
   - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L135
2. **`User`** 클래스 구조 확인
   - 실제로 User 클래스는 Meta 클래스를 제외한 코드가 없고 AbstractUser 클래스를 상속받고 있다.
   - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L389
3. **`AbstractUser`** 클래스 구조 확인
   - 클래스 변수 명들을 확인해보면 회원수정 페이지에서 봤던 필드들과 일치한다는 것을 확인할 수 있다.
   - admin 인터페이스에서 사용되는 ModelForm과 동일
   - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L321
4. 마지막으로 공식문서의 User 모델 Fields확인
   - https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model



# **비밀번호 변경**

## PasswordChangeForm

- 사용자가 비밀번호를 변결할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 한다.
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 `SetPasswordForm`을 상속받는 서브 클래스이다.



## 비밀번호 변경 시 세션 무효화 방지

### `update_session_auth_hash(request, user)`

- 현재 요청(current request)과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져오고, session hash를 적절하게 업데이트
- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태를 유지할 수 없기 때문이다.
- 암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session을 업데이트 해야한다.