# Generated by Django 4.2.4 on 2023-08-26 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0022_friendship_customuser_delete_frendshipdetails_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]