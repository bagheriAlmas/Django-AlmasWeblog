# Generated by Django 4.1.7 on 2023-03-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default_image.png', null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
