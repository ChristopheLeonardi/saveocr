from django.db import models
from django.conf import settings
import uuid
import os
from exiffield.fields import ExifField
from exiffield.getters import exifgetter, Orientation

# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    fpath = os.path.join(settings.MEDIA_ROOT , filename)
    print(fpath)
    return filename



class SearchText(models.Model):
    text_search = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.text_search

class Upload_Image(models.Model):
    image = models.FileField(upload_to=get_file_path, null=True, blank=True)
    orientation = models.CharField(editable=False, max_length=100, default="")
    exif = ExifField(
        source='image',
        denormalized_fields={
            'orientation': exifgetter(Orientation),
        },
    )

    def __str__(self):
        return self.image


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Author(models.Model):
    dates_biography = models.TextField()
    insi_number = models.TextField()
    author = models.TextField()
    biography = models.TextField()
    author_id = models.BigIntegerField(primary_key=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FtOtherArtwork(models.Model):
    copy = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_other_artwork'


class MusicArtwork(models.Model):
    name = models.TextField(blank=True, null=True)
    music_artwork_link = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    date_composition = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    intrumentation = models.TextField(blank=True, null=True)
    first_execution = models.TextField(blank=True, null=True)
    informations = models.TextField(blank=True, null=True)
    artwork_id = models.BigIntegerField(primary_key=True)
    author = models.TextField(blank=True, null=True)
    author_0 = models.ForeignKey(Author, models.DO_NOTHING, db_column='author_id', blank=True, null=True)  # Field renamed because of name conflict.
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'music_artwork'


class OcrUploadImage(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ocr_upload_image'


class OtherArtwork(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    details_author = models.TextField(blank=True, null=True)
    period_creation = models.TextField(blank=True, null=True)
    creation_year = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    conservation_place = models.TextField(blank=True, null=True)
    creation_place = models.TextField(blank=True, null=True)
    link_image = models.TextField(blank=True, null=True)
    other_artwork_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'other_artwork'


class RejectedArtwork(models.Model):
    rejected_name = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    artwork = models.ForeignKey(MusicArtwork, models.DO_NOTHING, blank=True, null=True)
    rejected_artwork_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rejected_artwork'


class RejectedAuthor(models.Model):
    rejected_name = models.TextField()
    author = models.TextField(blank=True, null=True)
    author_0 = models.ForeignKey(Author, models.DO_NOTHING, db_column='author_id', blank=True, null=True)  # Field renamed because of name conflict.
    rejected_author_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rejected_author'


class WikidataAuthor(models.Model):
    wikidata_author_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    dates_biography = models.CharField(max_length=255, blank=True, null=True)
    insi_number = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    wiki_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wikidata_author'
