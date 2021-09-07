from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     # selct name이 key값, ↓ option value 값
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGION_D = 'gm'
#     REGION_E = 'bs'
#     REGION_CHOICES = [
#         # 사용자에게 출력되는 부분(형식) 
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#         (REGION_D, '구미'),
#         (REGION_E, '부산'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select)


# class ArticleForm(forms.ModelForm):

#     class Meta:
#         model = Article
#         # fields = ('title', 'content',)
#         fields = '__all__'
#         # exclude = ('title',)


# Widget 설정하기
class ArticleForm(forms.ModelForm): 
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class': 'mt-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'mt-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )


    class Meta:
        model = Article
        fields = '__all__'