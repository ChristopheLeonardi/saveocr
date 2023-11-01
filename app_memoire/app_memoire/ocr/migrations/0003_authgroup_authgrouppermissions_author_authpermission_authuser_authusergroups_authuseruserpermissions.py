# Generated by Django 3.1.6 on 2023-05-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_auto_20230530_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('dates_biography', models.TextField()),
                ('insi_number', models.TextField()),
                ('author', models.TextField()),
                ('biography', models.TextField()),
                ('author_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FtOtherArtwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copy', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ft_other_artwork',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicArtwork',
            fields=[
                ('name', models.TextField(blank=True, null=True)),
                ('music_artwork_link', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('date_composition', models.TextField(blank=True, null=True)),
                ('duration', models.TextField(blank=True, null=True)),
                ('intrumentation', models.TextField(blank=True, null=True)),
                ('first_execution', models.TextField(blank=True, null=True)),
                ('informations', models.TextField(blank=True, null=True)),
                ('artwork_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('author', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'music_artwork',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OcrUploadImage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ocr_upload_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OtherArtwork',
            fields=[
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('details_author', models.TextField(blank=True, null=True)),
                ('period_creation', models.TextField(blank=True, null=True)),
                ('creation_year', models.TextField(blank=True, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('conservation_place', models.TextField(blank=True, null=True)),
                ('creation_place', models.TextField(blank=True, null=True)),
                ('link_image', models.TextField(blank=True, null=True)),
                ('other_artwork_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'other_artwork',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RejectedArtwork',
            fields=[
                ('rejected_name', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('rejected_artwork_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rejected_artwork',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RejectedAuthor',
            fields=[
                ('rejected_name', models.TextField()),
                ('author', models.TextField(blank=True, null=True)),
                ('rejected_author_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rejected_author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WikidataAuthor',
            fields=[
                ('wikidata_author_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('biography', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('dates_biography', models.CharField(blank=True, max_length=255, null=True)),
                ('insi_number', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.CharField(blank=True, max_length=255, null=True)),
                ('wiki_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'wikidata_author',
                'managed': False,
            },
        ),
    ]
