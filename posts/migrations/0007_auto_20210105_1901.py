# Generated by Django 3.1.4 on 2021-01-05 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_type',
            new_name='_type',
        ),
    ]
