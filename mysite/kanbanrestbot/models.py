# https://www.youtube.com/watch?v=fGXqTnWAFOo

from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.category_name

class Status(models.Model):
    status_name = models.CharField(max_length=50)
    status_slug = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.status_name

class Task(models.Model):
    task_name = models.CharField(max_length=800)
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField(default=1)
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    task_status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.task_name