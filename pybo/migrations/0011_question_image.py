# Generated by Django 3.2.5 on 2021-07-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
