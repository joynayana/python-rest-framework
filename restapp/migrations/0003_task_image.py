# Generated by Django 3.2.13 on 2022-05-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Images/Noimg.jpg', upload_to='Images/'),
        ),
    ]
