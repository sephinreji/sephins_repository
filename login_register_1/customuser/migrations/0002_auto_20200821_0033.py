# Generated by Django 3.1 on 2020-08-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BigIntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
