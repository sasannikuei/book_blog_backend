# Generated by Django 5.1.4 on 2024-12-14 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='release_date',
        ),
    ]
