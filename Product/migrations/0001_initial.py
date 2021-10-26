# Generated by Django 3.1.7 on 2021-04-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=15)),
                ('price', models.FloatField(max_length=15)),
            ],
        ),
    ]
