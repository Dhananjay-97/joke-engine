# Generated by Django 4.2.3 on 2023-07-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=50)),
                ('response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
    ]
