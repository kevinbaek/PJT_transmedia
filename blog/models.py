from django.db import models
from crawler.models import *

# Create your models here.

class Post(models.Model):
    target_url = models.URLField()
    kor_title = models.TextField()
    eng_content = models.TextField()
    kor_content = models.TextField()
    image_url =models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.kor_title = Translator(Crawler(self.target_url))[1]
        self.eng_content = Crawler(self.target_url)[0]
        self.kor_content = Translator(Crawler(self.target_url))[0]
        self.image_url = Crawler(self.target_url)[3]

        return super().save(*args, **kwargs)
