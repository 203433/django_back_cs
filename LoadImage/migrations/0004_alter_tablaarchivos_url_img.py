# Generated by Django 4.0.1 on 2022-02-05 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoadImage', '0003_alter_tablaarchivos_url_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaarchivos',
            name='url_img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/img/'),
        ),
    ]
