from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='news',
        verbose_name='Фото'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Новости'
        verbose_name_plural = 'Новости'

