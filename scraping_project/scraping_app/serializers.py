from rest_framework import serializers
from .models import WebsiteList


class WebsiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteList
        fields = ['website_url', 'category']
