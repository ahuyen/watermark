# Generated by Django 2.0.1 on 2018-02-14 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.WatermarkUser')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.UserCard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.WatermarkUser')),
            ],
        ),
    ]