# Generated by Django 4.2 on 2025-01-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_born',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
