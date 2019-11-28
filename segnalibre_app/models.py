from django.db import models
from computedfields.models import ComputedFieldsModel, computed

# Create your models here.
class Book(ComputedFieldsModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_url = models.URLField(null=True)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateField()
    pages = models.IntegerField()
    position = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title

    @computed(models.CharField(max_length=32, default='uncompleted'))
    def status(self):
        if self.position == self.pages:
            return 'completed'
        else:
            return 'uncompleted'
