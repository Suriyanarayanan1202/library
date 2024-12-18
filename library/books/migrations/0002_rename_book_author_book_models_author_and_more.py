# Generated by Django 4.2.16 on 2024-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_models',
            old_name='book_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book_models',
            old_name='book_name',
            new_name='isbn',
        ),
        migrations.RenameField(
            model_name='book_models',
            old_name='book_pages',
            new_name='pages',
        ),
        migrations.AddField(
            model_name='book_models',
            name='publisher',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book_models',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
