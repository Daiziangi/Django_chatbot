from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class Dialog(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    content = models.TextField()  # 消息内容
    timestamp = models.DateTimeField(auto_now_add=True)  # 发送时间戳

    def __str__(self):
        return self.content
    
class BrowseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户
    page = models.CharField(max_length=100)  # 浏览的页面
    timestamp = models.DateTimeField(auto_now_add=True)  # 浏览时间

    def __str__(self):
        return f'{self.user.username} - {self.page}'

    class Meta:
        ordering = ['-timestamp']  # 默认按照时间戳逆序排序