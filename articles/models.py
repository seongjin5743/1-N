from django.db import models

# 게시글(Article) 모델 정의
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)  # 생성 시간 (자동 추가)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)  # 수정 시간 (자동 갱신)

    # comment_set: Comment 모델과의 역참조 관계 (Django에서 자동 생성)

# 댓글(Comment) 모델 정의
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 게시글과의 외래키 관계 (게시글 삭제 시 댓글도 삭제)

    # article_id: Article 모델의 id를 참조 (Django에서 자동 생성)