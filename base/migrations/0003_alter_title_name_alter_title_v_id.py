# Generated by Django 4.1.7 on 2023-02-25 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_title_color_title_v_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='title',
            name='v_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
