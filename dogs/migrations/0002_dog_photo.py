# Generated by Django 4.2.2 on 2023-07-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='photo',
            field=models.ImageField(null=True, upload_to='dogs/'),
        ),

    ]