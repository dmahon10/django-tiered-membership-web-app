# Generated by Django 3.1.4 on 2020-12-24 10:39

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('author', models.CharField(max_length=100)),
                ('excerpt', models.TextField(max_length=300)),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='FreeArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.article')),
            ],
            bases=('articles.article',),
        ),
        migrations.CreateModel(
            name='PremiumArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.article')),
            ],
            options={
                'permissions': [('premium_member', 'premium article permission')],
            },
            bases=('articles.article',),
        ),
    ]