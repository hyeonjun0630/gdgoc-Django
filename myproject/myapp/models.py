from django.db import models

class Post(models.Model): # POST 테이블 생성
    title = models.CharField(max_length=100) # 반드시 길이 지정 / null=true, blank=true, default="" 옵션 넣을 수 있음
    content = models.TextField() # 반드시 지정은 x
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)