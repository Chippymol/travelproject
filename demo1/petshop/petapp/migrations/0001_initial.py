# Generated by Django 4.2 on 2023-06-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teammember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=250)),
                ('memberimage', models.ImageField(upload_to='pics2')),
                ('memberdesc', models.TextField()),
            ],
        ),
    ]