# Generated by Django 5.0 on 2024-12-28 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='target_word_count',
        ),
    ]
