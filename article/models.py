from django.db import models
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now=True,verbose_name="Oluşturma Zamanı")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-created_date"]
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name ="Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50 ,verbose_name ="İsim")
    comment_content = models.CharField(max_length = 200,verbose_name ="İçerik")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ["-comment_date"]

