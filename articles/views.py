from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# 게시글 생성 함수
def create(request):
    if request.method == 'POST':  # POST 요청일 경우
        form = ArticleForm(request.POST)  # 전달받은 데이터를 폼에 넣기기
        if form.is_valid():  # 폼 데이터가 유효한지 검증
            form.save()  # 유효하다면 저장
            return redirect('articles:index')  # 저장 후 index 페이지로 리다이렉트
    else:
        form = ArticleForm()  # 빈 폼 생성

    context = {
        'form': form,  # 템플릿에 전달할 폼 객체
    }
    return render(request, 'create.html', context)  # create.html 렌더링

# 게시글 목록 조회 함수
def index(request):
    articles = Article.objects.all()  # 모든 게시글 조회

    context = {
        'articles': articles,  # 템플릿에 전달할 게시글 리스트
    }

    return render(request, 'index.html', context)  # index.html 렌더링

# 게시글 상세 조회 함수
def detail(request, id):
    article = Article.objects.get(id=id)  # 특정 id의 게시글 조회
    form = CommentForm()  # 댓글 작성 폼 생성
    context = {
        'article': article,  # 템플릿에 전달할 게시글 객체
        'form': form,  # 템플릿에 전달할 댓글 폼
    }

    return render(request, 'detail.html', context)  # detail.html 렌더링

# 게시글 수정 함수
def update(request, id):
    article = Article.objects.get(id=id)  # 특정 id의 게시글 조회
    if request.method == 'POST':  # POST 요청일 경우
        form = ArticleForm(request.POST, instance=article)  # 기존 게시글 데이터를 폼에 넣기
        if form.is_valid():  # 폼 데이터가 유효한지 검증
            form.save()  # 유효하다면 저장
            return redirect('articles:detail', id=id)  # 저장 후 상세 페이지로 리다이렉트
    else:
        form = ArticleForm(instance=article)  # 기존 게시글 데이터를 폼에 넣기기

    context = {
        'form': form,  # 템플릿에 전달할 폼 객체
    }
    return render(request, 'update.html', context)  # update.html 렌더링

# 게시글 삭제 함수
def delete(request, id):
    article = Article.objects.get(id=id)  # 특정 id의 게시글 조회
    article.delete()  # 게시글 삭제
    return redirect('articles:index')  # 삭제 후 index 페이지로 리다이렉트

# 댓글 생성 함수
def comment_create(request, article_id):
    if request.method == 'POST':  # POST 요청일 경우
        form = CommentForm(request.POST)  # 전달받은 데이터를 폼에 바인딩
        if form.is_valid():  # 폼 데이터가 유효한지 검증
            comment = form.save(commit=False)  # 데이터 저장 전 객체 반환
            article = Article.objects.get(id=article_id)  # 댓글이 달릴 게시글 조회
            comment.article = article  # 댓글에 게시글 연결
            comment.save()  # 댓글 저장
            
        return redirect('articles:detail', id=article_id)  # 저장 후 상세 페이지로 리다이렉트
    else:
        return redirect('articles:index')  # index 페이지로 리다이렉트

# 댓글 삭제 함수
def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)  # 특정 id의 댓글 조회
    comment.delete()  # 댓글 삭제

    return redirect('articles:detail', id=article_id)  # 삭제 후 상세 페이지로 리다이렉트