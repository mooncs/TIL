import random
from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request(해당 이름이 아니어도 되지만 권장사항)
    return render(request, 'articles/index.html') # render 첫번째 인자는 request


def greeting(request):
    foods = ['곰국', '김고추장', '장조림', '라면']
    info = {
        'name': 'kim',
        'age' : '21',
    }

    context = {
        'foods':foods,
        'info':info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods =['피자', '치킨', '초밥', '햄버거', '족발']
    pick = random.choice(foods)
    context = {
        'foods':foods,
        'pick':pick,
    }
    return render(request, 'articles/dinner.html', context)

def dtl_prctice(request):
    foods =['피자', '치킨', '초밥', '햄버거', '족발']
    fruits = ['사과', '망고', '복숭아', '딸기']
    user_list = []

    context = {
        'foods':foods,
        'fruits':fruits,
        'user_list':user_list,
    }
    return render(request, 'articles/dtl_practice.html', context)

def throw(request):
    return render(request, 'articles/throw.html')
    
def catch(request):
    message = request.GET.get('message')
    context = {
        'message':message,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name':name,
    }
    return render(request, 'articles/hello.html', context)

def hmk(request):
    posts =['피자', '치킨', '초밥', '햄버거', '족발']
    today = datetime(2020, 2, 2, hour=14, minute=2)
    context = {
        'posts':posts,
        'today':today,
    }
    return render(request, 'articles/hmk.html', context)