# Generated by Django 4.2.3 on 2023-09-19 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='image',
            new_name='resume',
        ),
    ]
