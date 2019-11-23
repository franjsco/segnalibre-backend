from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateField()
    pages = models.IntegerField()
    position = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title

