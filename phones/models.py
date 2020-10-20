from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs.keys() and 'name' in kwargs.keys():
            kwargs['slug'] = slugify(kwargs.get('name'))
        super(Phone, self).__init__(*args, **kwargs)
