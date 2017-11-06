from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=64,verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    def __str__(self):
        return self.username
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.TimeField(auto_now_add=True,null=True)
    author = models.ForeignKey("UserInfo",to_field="id")
    category = models.ForeignKey("Category",to_field="id")
    article_type = models.ForeignKey("ArticleType",to_field="id")
    def __str__(self):
        return self.title
class Category(models.Model):
    caption = models.CharField(max_length=16)
    def __str__(self):
        return self.caption
class ArticleType(models.Model):
    caption = models.CharField(max_length=16)
    def __str__(self):
        return self.caption