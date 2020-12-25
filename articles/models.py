import uuid
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

TIERS = (
    ("free", "FREE"),
    ("premium", "PREMIUM"),
)

class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    author = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=300)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    content = RichTextUploadingField()
    date_created = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''
        If duplicate titles, append an incrementing value to the slug
        '''
        initial_slug = slugify(self.title)
        queryset = Article.objects.all().filter(slug__iexact=initial_slug).count()
        queryset = PremiumArticle.objects.all().filter(slug__iexact=initial_slug).count()
        count = 0
        slug = initial_slug
        while(queryset):
            slug = initial_slug + '-' + str(count)
            count += 1
            queryset = Article.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug
        super(Article, self).save(*args, **kwargs)
    
    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
    
    
    
   
class FreeArticle(Article):
    tier = models.CharField(max_length=7, choices=TIERS, default="free", editable=False)
    def get_absolute_url(self):
        return reverse('free_article_detail', args=[str(self.slug)])


class PremiumArticle(Article):
    tier = models.CharField(max_length=7, choices=TIERS, default="premium", editable=False)
    class Meta:
        permissions = [
            ('premium_member', 'premium article permission')
        ]

    def get_absolute_url(self):
        return reverse('premium_article_detail', args=[str(self.slug)])


class Comment(models.Model):  
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    comment = models.CharField(max_length=255)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self): 
        return self.comment
