# Generated by Django 3.1 on 2020-10-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=120, unique=True)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField(default=100)),
            ],
        ),
    ]
