# Generated by Django 4.2 on 2025-01-09 12:49

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_date_born'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[users.validators.validate_email], verbose_name='E-mail'),
        ),
    ]