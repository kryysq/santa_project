from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    assigned_to = models.CharField(max_length=100, blank=True, null=True, verbose_name="Кому дарує")

    def __str__(self):
        return self.name
