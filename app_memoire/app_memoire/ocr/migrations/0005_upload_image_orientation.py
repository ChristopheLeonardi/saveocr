# Generated by Django 4.2.1 on 2023-07-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0004_searchtext_upload_image_exif'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_image',
            name='orientation',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
    ]
