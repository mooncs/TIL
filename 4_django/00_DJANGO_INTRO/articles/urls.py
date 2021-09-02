from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('dtl_pratice/', views.dtl_prctice, name='dtl_prctice'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # path('hello/<name>/', views.hello),   # str을 안써도 가능하지만, 명확히 하기 위해
    path('hello/<str:name>/', views.hello, name='hello'),
    path('hmk/', views.hmk, name='hmk'),
]
