# Generated by Django 5.1.3 on 2024-11-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_useraccount_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='firstname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
