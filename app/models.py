from django.db import models

class Person(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=130)
	email = models.EmailField(blank=True)
	job_title = models.CharField(max_length=30, blank=True)
	bio = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = "person"
		ordering = ['created_at']
		verbose_name = "person"
		verbose_name_plural = "person"
