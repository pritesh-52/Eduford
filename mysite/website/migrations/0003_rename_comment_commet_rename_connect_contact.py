# Generated by Django 4.0.4 on 2022-04-25 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comment',
            new_name='Commet',
        ),
        migrations.RenameModel(
            old_name='connect',
            new_name='Contact',
        ),
    ]
