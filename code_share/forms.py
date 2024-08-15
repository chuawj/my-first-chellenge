from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['title', 'language', 'code_snippet', 'price', 'description', 'uploaded_by']
        labels = {
            'title': '코드 제목',
            'language': '언어',
            'code_snippet': '코드 스니펫',
            'price': '가격',
            'description': '설명',
            'uploaded_by': '업로드한 사용자',
        }
