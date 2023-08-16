from django.db import models

# Create your models here.
class Website(models.Model):
    url = models.URLField()

class Keyword(models.Model):
    word = models.CharField(max_length=100)

class SearchResult(models.Model):
    website = models.ForeignKey(Website, on_delete= models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete= models.CASCADE)
    keyword_found = models.BooleanField(default=False)
    relative_info = models.TextField(blank=True)

