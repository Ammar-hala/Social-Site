# Generated by Django 3.1 on 2020-08-29 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='descriptions',
            new_name='description',
        ),
    ]