from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Biografy(models.Model):
    name = models.CharField('Автор', max_length=100)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    date_of_death = models.DateField('Дата смерти', null=True, blank=True)
    text = models.TextField('Имформация о жизни')

    def __str__(self): 
        return self.name


class Author(models.Model):
    first_name = models.CharField('Имя Автора', max_length=100)
    last_name = models.CharField('Фамилия Автора', max_length=100)
    name_url = models.CharField(verbose_name='Страница автора', max_length=30, unique=True)
    description = models.OneToOneField(
        Biografy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bio',
        verbose_name='Справка о писателе')

    def __str__(self): 
        return f'{self.first_name} {self.last_name}'


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