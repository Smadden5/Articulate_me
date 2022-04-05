class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "author ")
    title = models.CharField(max_length = 50,verbose_name = "title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="created")
    article_image = models.FileField(blank = True,null = True,verbose_name="image")
    slug = models.SlugField(unique=True, max_length=100)

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
    comment_author = models.CharField(max_length = 50,verbose_name = "name")
    comment_content = models.CharField(max_length = 200,verbose_name = "comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']