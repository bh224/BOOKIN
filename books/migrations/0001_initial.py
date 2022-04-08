# Generated by Django 4.0.3 on 2022-04-08 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRentByUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exp_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('review_rating', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('book_img', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('book_views', models.IntegerField(default=0)),
                ('is_rented', models.BooleanField(default=False)),
                ('like_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
