# Generated by Django 3.1.4 on 2021-01-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210129_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='oder',
            name='status',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]