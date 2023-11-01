# Generated by Django 4.2.1 on 2023-07-14 07:49

from django.db import migrations, models
import exiffield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0003_authgroup_authgrouppermissions_author_authpermission_authuser_authusergroups_authuseruserpermissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_search', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='upload_image',
            name='exif',
            field=exiffield.fields.ExifField(default={}, editable=False),
        ),
    ]
