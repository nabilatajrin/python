from django.db import models
from django.urls import reverse

#create your models here
class Product(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank = False, null = False)
    featured    = models.BooleanField() #null = True, .default = True

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"


