# Generated by Django 2.2 on 2020-06-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200626_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
