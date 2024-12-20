# Generated by Django 4.2.16 on 2024-12-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200, null=True)),
                ('book_author', models.CharField(max_length=200, null=True)),
                ('book_price', models.IntegerField(default=0)),
                ('book_pages', models.IntegerField(default=0)),
            ],
        ),
    ]
