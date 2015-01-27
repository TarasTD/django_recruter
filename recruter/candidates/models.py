from django.db import models


class Technology(models.Model):
    tech = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tech

class Candidate(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    current_company = models.CharField(max_length=30)
    date_added = models.DateField(auto_now=True)
    latest_changes = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    comment = models.TextField()
    EXPERIENCE_CHOICES = (
        ('WJ', 'Weak Junior'),
        ('J', 'Junior'),
        ('SJ', 'Strong Junior'),
        ('WM', 'Weak Middle'),
        ('M', 'Middle'),
        ('SM', 'Strong Middle'),
        ('WS', 'Weak Senior'),
        ('S', 'Senior'),
        ('SS', 'Strong Senior'),
        )
    experience = models.CharField(max_length=2,
                                  choices=EXPERIENCE_CHOICES)

    specification = models.ManyToManyField(Technology)

    def __unicode__(self):
        return self.name + self.surname
