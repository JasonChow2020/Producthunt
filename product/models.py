from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()
    pub_date = models.DateTimeField()
    vote_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='image/')
    icon = models.ImageField(upload_to='image/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) #key from other models, if user delete, all delete

    def __str__(self):
        return self.title  # show title in the admin UI

    def abbrev(self):
        return self.body[:100]  # shorten to 100 characters

    def date(self):
        return self.pub_date.strftime('%b %e %Y')  # month, date , Year