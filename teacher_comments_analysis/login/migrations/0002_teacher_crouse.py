# Generated by Django 2.1.7 on 2019-04-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='crouse',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]
