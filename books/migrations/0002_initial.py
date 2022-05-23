# Generated by Django 4.0.3 on 2022-04-18 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookstore.bookstoremodel'),
        ),
    ]
