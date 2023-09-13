from django.db import models

class Country(models.Model):
    # United Kingdom of Great Britain and Northern Ireland
    name = models.CharField(max_length=58,
                            verbose_name="Country name",
                            help_text="Enter a country name")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']