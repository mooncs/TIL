from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import CustomUserChangeForm

# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/index.html', context)


@require_http_methods(['POST', 'GET'])
def login(request):
    # 로그인이 되어있으면, 로그인을 할 필요가 없다.
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 검증을 통과하면
        if form.is_valid():
            # 로그인
            # login()으로 함수명을 지정했기 때문에 충돌이 일어난다.
            # 이를 방지하기 위해 django의 login함수를 auth_login으로 명명
            auth_login(request, form.get_user())
            # 인증 성공 시 사용자가 redirect 되어야하는 경로는 `"next"`라는 쿼리 문자열 매개변수에 저장된다.
            # /accounts/login/?next=/articles/create
            # 단축 평가 활용
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    # 로그인이 되어있으면
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['POST', 'GET'])
def signup(request):
    # 로그인이 되어있으면, 회원가입을 할 필요가 없다.
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # UserCreationForm의 save 메서드는 user를 return한다.
            user = form.save()
            # 회원가입 한 다음 바로 로그인하기
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
    

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        # session도 지우고 싶다면, logout도 진행하면 된다.
        # logout을 하고 delete를 할 수는 없으므로 순서 주의!!
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['POST', 'GET'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 수정은 instance가 필요하다.
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        # PasswordChangeForm 첫 인자는 무조건 request.user !!!
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 비밀번호 변경 후 logout이 된다 → session에 문제가 생겼다.
            # 새로운 password hash로 session을 업데이트
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # PasswordChangeForm 첫 인자는 무조건 request.user !!!
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)