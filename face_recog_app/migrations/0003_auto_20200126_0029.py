# Generated by Django 2.1.7 on 2020-01-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recog_app', '0002_auto_20200126_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recogedimageuploadedimage',
            name='people',
        ),
        migrations.AddField(
            model_name='recogedimageuploadedimage',
            name='name',
            field=models.CharField(default='nope', max_length=200, verbose_name='name'),
            preserve_default=False,
        ),
    ]
