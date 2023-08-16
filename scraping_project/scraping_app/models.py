from django.db import models


class Website(models.Model):
    url = models.URLField()


class Keyword(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SearchResult(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    keyword_found = models.BooleanField(default=False)
    relative_info = models.TextField(blank=True)
