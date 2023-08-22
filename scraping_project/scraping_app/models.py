from django.db import models


# class Search(models.Model):
#     website_url = models.URLField()
#     keyword = models.CharField(max_length=255)
#     keyword_found = models.BooleanField(default=False)
#     relative_info = models.TextField(blank=True)


class WebsiteList(models.Model):
    website_url = models.URLField()
    category = models.CharField(max_length=255)

    class Meta:
        db_table = 'WebsiteList'
