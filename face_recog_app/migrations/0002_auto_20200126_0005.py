# Generated by Django 2.1.7 on 2020-01-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recogedimageuploadedimage',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]