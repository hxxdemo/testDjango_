from django.db import models

from django.utils.timezone import now

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100,null=True)

#     def __str__(self):
#         return self.name
        
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_time = models.DateTimeField(null=False, default=now)
    #category = models.ForeignKey(to=Category, related_name='cate')
    TAG_CHOICES = (
        ('python','python'),
        ('web', 'web'),
        ('life', 'life')
        )  
    tag = models.CharField(choices=TAG_CHOICES, max_length=10, null=True, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(null=False)
    comment_time = models.DateTimeField(default=now,null=False)

    def __str__(self):
        return self.name
# class Belong_cate(models.Model):
#     select_article = models.ForeignKey(to=Article, related_name='select_article')
#     SELECT_REASON = (
#         ('Python', 'Python'),
#         ('Django', 'Django'),
#         ('JavaScript','JavaScript')
#         )
#     select_reason = models.CharField(choices=SELECT_REASON, max_length=50, null=False)
#     def __str__(self):
#         return self.select_article +' - ' + self.select_reason
