# Generated by Django 4.0.1 on 2022-02-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoadImage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaarchivos',
            name='url_img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/'),
        ),
    ]
