# Generated by Django 4.1.2 on 2022-10-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpeta1', '0004_alter_members_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]