# Generated by Django 3.1 on 2021-08-07 13:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_blog', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('snippet_blog', models.CharField(default='Add a Snippet.', max_length=500)),
                ('author_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
