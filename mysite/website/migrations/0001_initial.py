# Generated by Django 3.1.4 on 2021-05-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=40)),
            ],
        ),
    ]
