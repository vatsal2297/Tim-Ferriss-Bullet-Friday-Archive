# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tff5BulletEmails(models.Model):
    email_message_id = models.CharField(unique=True, max_length=255)
    email_date = models.DateTimeField()
    email_title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tff_5bullet_emails'
        unique_together = (('id', 'email_message_id'),)
        verbose_name = 'TFF 5Bullet Email'
        verbose_name_plural = 'TFF 5Bullet Emails'


class TffBullets(models.Model):
    tff_email = models.ForeignKey(Tff5BulletEmails, models.DO_NOTHING)
    bullet_heading = models.CharField(max_length=255)
    bullet_content = models.TextField()
    searchable_bullet_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'tff_bullets'
        verbose_name = 'TFF Bullet'
        verbose_name_plural = 'TFF Bullets'
