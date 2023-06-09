# Generated by Django 4.1.7 on 2023-03-13 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articles', to='articles.article')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
