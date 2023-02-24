# Generated by Django 4.1 on 2023-02-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('book_pages', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
