
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify 
# Create your models here.
import random
import string

class Address(models.Model):
    street = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Author address entries"

    def __str__(self):
        return f"{self.street} - - {self.postal_code}"
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    #human readable representation of the model's instance 
    def __str__(self):
        return f"{self.first_name}+{self.last_name}"


class Book_stem(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]  
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_BestSelling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,null=False, db_index=True)


    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    


    def __str__(self):
        return f"{self.title} -  {self.rating}"

