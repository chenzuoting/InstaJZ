# Generated by Django 3.0.8 on 2020-07-13 05:54

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='static/images/posts')),
            ],
        ),
    ]
