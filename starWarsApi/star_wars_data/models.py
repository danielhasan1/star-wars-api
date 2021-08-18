from django.db import models

# Create your models here.
class StarWarsPlanets(models.Model):
    title = models.CharField(max_length=240)
    my_title = models.CharField(max_length=240,blank=True,null=True)
    favourite = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    @property
    def title_count_ret(self):
        return StarWarsPlanets.objects.count()