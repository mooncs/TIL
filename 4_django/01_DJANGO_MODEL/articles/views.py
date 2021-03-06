# 명시적 상대경로
from .models import Article
from django.shortcuts import render

# Create your views here.
def index(request):
    # 작성한 모든 게시글을 출력
    # 1. 모든 게시글 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 게시글 작성 페이지를 render하는 views
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new로부터 title과 content를 받아서 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # # 3
    # # 유효성 검사를 할 틈이 없다.
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')


def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
