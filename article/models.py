from django.db import models
from django.contrib.auth import get_user_model

# from users.models import CustomUser
# Status = (
#     (0, “Draft”),
#     (1, Publish))

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "author ")
    # author = models.ForeignKey(CustomUser,on_delete = models.CASCADE,verbose_name = "author ")
    title = models.CharField(max_length = 50,verbose_name = "title")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="created_date")
    article_image = models.FileField(blank = True,null = True,verbose_name="article_image")
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "article",related_name="comment")
    comment_author = models.CharField(max_length = 50,verbose_name = "comment_author")
    comment_content = models.CharField(max_length = 200,verbose_name = "comment_content")
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-created_date']


# class Categories():
#     title = (Charfield)
#     slug = (SlugField)
#     updated = (DateTimeField)(auto_now_add=True)
#     content = (Charfield)
    
#     def__str__(self)

#     def __str__(self):
#         return self.title
    
