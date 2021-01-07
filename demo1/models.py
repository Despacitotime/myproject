from django.db import models


# Create your models here.
# 相当于一个实体类，对应于数据库中的表
class Demo1(models.Model):
    # 标题
    title = models.CharField(max_length=30)
    # 内容
    content = models.TextField()
