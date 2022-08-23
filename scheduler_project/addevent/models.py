from django.db import models

class Event(models.Model):
    #'title', 'author', 'date', 'description'
    title = models.CharField(max_length=30, verbose_name='Название мероприятия')
    author = models.CharField(max_length=30, verbose_name='Ответсвенное лицо')
    date = models.DateField(verbose_name='Дата проведения')
    description = models.TextField(verbose_name='Дополнительная информация', blank=True)

    def __str__(self):
        return '%s, %s' % (self.title, self.date)
