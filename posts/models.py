from django.db import models
from users.models import User, NULLABLE


class Post(models.Model):

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст поста')
    image = models.ImageField(verbose_name='Изображение', upload_to="posts/image", **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста', **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания поста')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения поста')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Комментарий к посту')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', **NULLABLE)
    text = models.TextField(verbose_name='Текст комментария')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания комментария')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text}'
