from django.db import models

class Code(models.Model):
    title = models.CharField(max_length=200, verbose_name='코드 제목')
    language = models.CharField(max_length=50, verbose_name='언어')  
    code_snippet = models.TextField(verbose_name='코드 스니펫')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='가격')
    description = models.TextField(verbose_name='설명')
    uploaded_by = models.CharField(max_length=100, verbose_name='업로드한 사용자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='업로드 날짜')

    def __str__(self):
        return self.title
