# Generated by Django 2.1 on 2019-04-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]
