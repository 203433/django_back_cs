# Generated by Django 4.0.1 on 2022-02-02 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TablaArchivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_img', models.CharField(max_length=50)),
                ('url_img', models.CharField(max_length=100)),
                ('format_img', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'tabla_archivos',
                'managed': True,
            },
        ),
    ]
