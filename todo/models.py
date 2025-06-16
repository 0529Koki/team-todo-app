from django.db import models

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    avatar_url = models.URLField(blank=True, null=True)  # アバター画像URL（任意）

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    assignee = models.ForeignKey(Member, on_delete=models.CASCADE)  # 担当者
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Create your models here.
