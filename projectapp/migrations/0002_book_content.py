# Generated by Django 5.0.6 on 2024-06-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='ajoyib kitob kitob haqida kup narsa aytish mumkin'),
            preserve_default=False,
        ),
    ]
