from django.db import models

# Create your models here.
class News_post(models.Model):
	title = models.CharField('Название новости', max_length=150)
	short_description = models.CharField('Краткое описание новости', max_length=250)
	text = models.TextField('Новость')
	author = models.CharField('Автор', max_length=50)
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
