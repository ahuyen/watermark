# Generated by Django 2.0.1 on 2018-02-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20180222_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='name',
            field=models.CharField(default='New wallet', max_length=100),
        ),
    ]
