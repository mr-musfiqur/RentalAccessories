# Generated by Django 3.1.7 on 2021-04-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
