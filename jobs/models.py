from django.db import models
import datetime


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    date_from = models.DateField(default=datetime.date.today)
    date_to = models.DateField(blank=True, null=True, default=datetime.date.today)

    def __str__(self):
        return self.summary[:15]

    def date_from_pretty(self):
        return self.date_from.strftime('%d/%Y')

    def date_to_pretty(self):
        if self.date_to is None:
            return "Nadal"
        return self.date_to.strftime('%d/%Y')
