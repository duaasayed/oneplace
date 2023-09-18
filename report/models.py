from django.db import models
from accounts.models import User

class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    posted_at = models.DateField(null=True)
    job_type = models.CharField(max_length=150, null=True)
    experience_level = models.CharField(max_length=150, null=True)
    medium = models.CharField(max_length=150)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Application(models.Model):
    class ApplicationStatus(models.IntegerChoices):
        NoResponse = (0, 'No Response')
        VIEWED = (1, 'Viewed')
        CONTACTED = (2, 'Contacted')
        INTERVIEWED = (3, 'Interviewed')
        ACCEPTED = (4, 'Accepted')
        REJECTED = (5, 'Rejected')


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    posted_at = models.DateField(null=True)
    applied_at = models.DateField()
    job_type = models.CharField(max_length=150, null=True)
    experience_level = models.CharField(max_length=150, null=True)
    medium = models.CharField(max_length=150)
    link = models.URLField(max_length=500)
    status = models.IntegerField(choices=ApplicationStatus.choices)

    def __str__(self):
        return self.title
