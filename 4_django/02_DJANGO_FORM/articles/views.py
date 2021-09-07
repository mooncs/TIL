from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# new와 create 하나로 합치기
@require_http_methods(['GET', 'POST'])
def create(request):
    # 왜 POST를 먼저 분기하는가!! → if GET, else를 하면 POST가 아니라도 핵심 데이터에 접근할 수 있게 된다.
    # create → 데이터를 작성
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 저장한 객체를 생성
            article = form.save()
            return redirect('articles:detail', article.pk)
    # new → 단순 조회
    else:   # GET
        # 사용자에게 데이터를 받을 빈 form 만들기
        form = ArticleForm()
    # 유효성 검사를 실패할 것을 대비하여 else문 밖에 작성!!!
    # 유효성 검사를 실패시 error message를 넘겨준다.
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    # 데이터가 없을 경우 500 error 발생, 불명확한 error
    # article = Article.objects.get(pk=pk)
    # 데이터가 없을 경우 404 error 발생, 명확한 error
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')

    # @require_POST를 이용해 필요 없어진 코드----
    # if request.method == 'POST':
    #     article.delete()
    #     return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)


# edit과 update 하나로 합치기
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    # updates
    if request.method == 'POST':
        # 수정하기 위해서는 instance가 필요, instance가 없으면 create로 인식!!!
        # form = ArticleForm(data=request.POST, instance=article)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # edit
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)