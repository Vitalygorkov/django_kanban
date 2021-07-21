from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    task_name = models.CharField(max_length=800)
    task_text = models.CharField(max_length=200)
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.task_name
