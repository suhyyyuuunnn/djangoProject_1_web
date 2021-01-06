from django.utils import timezone
from django.db import models
from django.urls import reverse
from django_summernote.utils import get_attachment_storage, get_attachment_upload_to


class Post(models.Model):
    class Meta:
        ordering = ['-created_at']

    POST_TYPE = [
        (0, "해킹"),
        (1, "개발"),
        (2, "보안"),
        (3, "책")
    ]

    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField()
    view_count = models.IntegerField(default=0, verbose_name="조회수")
    file = models.FileField(upload_to="posts/file", blank=True)
    like_count = models.IntegerField(default=0, verbose_name="추천수")
    link = models.URLField(null=True, blank=True, verbose_name="참조링크")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트시간")
    _type = models.PositiveSmallIntegerField(choices=POST_TYPE, verbose_name="게시글타입")

    def value(self):
        return self._type

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:show', args=[self.pk])
