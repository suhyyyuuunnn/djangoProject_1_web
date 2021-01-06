from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    _type = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="게시글 종류",
        choices=Post.POST_TYPE,
        required=True
    )

    class Meta:
        model = Post
        fields = ['title', '_type', 'content',  'file']
        labels = {
            'title': '제목',
            'content': '내용',
            'file': '게시글 파일'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': SummernoteWidget(),
        }