# Generated by Django 4.2 on 2023-04-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='username_5fe9408b8f4b', max_length=100),
        ),
    ]