from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='categories/%Y/%m/%d/',blank=True,null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'



class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_date']


class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



