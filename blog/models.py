from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #This field links the Post and Category models and creates a relationship between the two tables.
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #One post can have many comments (one-to-many) / models.CASCADE to delete all comments related to a post when the post is deleted
    post = models.ForeignKey('Post', on_delete=models.CASCADE)