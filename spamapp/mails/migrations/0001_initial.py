# Generated by Django 3.2.9 on 2022-04-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_spam', models.BooleanField(default=False)),
            ],
        ),
    ]