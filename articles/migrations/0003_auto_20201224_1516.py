# Generated by Django 3.1.4 on 2020-12-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201224_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freearticle',
            name='tier',
            field=models.CharField(choices=[('free', 'FREE'), ('premium', 'PREMIUM')], default='free', max_length=7),
        ),
    ]