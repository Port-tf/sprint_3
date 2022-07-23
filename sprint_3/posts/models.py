
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    name = models.CharField('Автор произведения', max_length=100)
    name_url = models.CharField(verbose_name='Страница автора', max_length=30)
    description = models.TextField(blank=True, verbose_name='Справка о писателе')

    def __str__(self): 
        return self.name[:20]


class Poem(models.Model):
    text = models.TextField(verbose_name='Стихи')
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='poems',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='poems',
        verbose_name='Любитель поэзии'
    )

    class Meta:
        verbose_name = 'Произведение' 
        verbose_name_plural = 'Произведения' 

 
    def __str__(self): 
        return self.text[:40] 