# Generated by Django 4.0.5 on 2022-07-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dozoo_app', '0002_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
