# Generated by Django 4.1.2 on 2022-10-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpeta1', '0002_members_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='adress',
            field=models.CharField(default='adress', max_length=255),
        ),
        migrations.AddField(
            model_name='members',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
