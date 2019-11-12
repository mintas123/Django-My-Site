from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 100:
            return self.body[:100]+'...'
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b  %Y')
