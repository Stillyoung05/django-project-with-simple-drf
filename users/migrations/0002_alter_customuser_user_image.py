# Generated by Django 5.0.1 on 2024-01-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(default='media/default_user_image.jpg', upload_to='media/'),
        ),
    ]
