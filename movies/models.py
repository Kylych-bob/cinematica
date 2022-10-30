from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name = 'Категория')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = [] # сортировка по 
    

class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tagline = models.CharField(max_length=100, default='', verbose_name='Слоган')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(verbose_name='Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField(default=2019, verbose_name='Дата выхода')
    country = models.CharField(max_length=30, verbose_name='Страна')
    directors = models.ManyToManyField(to=Actor, verbose_name='Режиссер', related_name='film_director')
    actors = models.ManyToManyField(to=Actor, verbose_name='Актеры', related_name='film_actor')
    genres = models.ManyToManyField(to=Genre, verbose_name='Жанр')
    world_premiere = models.DateField(default=date.today, verbose_name='Премьера в мире')
    budget = models.PositiveIntegerField(default=0, help_text='указать сумму в $', verbose_name='Бюджет')
    fees_in_USA = models.PositiveIntegerField(default=0, verbose_name='Сборы в США', help_text='указать сумму в $')
    fees_in_world = models.PositiveIntegerField(default=0, verbose_name='Сборы в мире', help_text='указать сумму в $')
    category = models.ForeignKey(to=Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(verbose_name='Черновик', default=False)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='movie_shots/', verbose_name='Изображение')
    movie = models.ForeignKey(to=Movie, verbose_name='Фильм', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name='Значение', default=0)
    
    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинги'


class Rating(models.Model):
    ip = models.CharField(max_length=15, verbose_name='IP адрес')
    start = models.ForeignKey(to=RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(verbose_name='Имя', max_length=100)
    message = models.TextField(verbose_name='Сообщение', max_length=5000)
    # Запись будет ссылатся в этой же таблице self
    text = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(to=Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'