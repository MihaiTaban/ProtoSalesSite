# Generated by Django 3.1.6 on 2021-02-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20210207_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skibootsdb',
            name='Availability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skibootsdb',
            name='Size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skidb',
            name='Availability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skidb',
            name='Size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snowboardbootsdb',
            name='Availability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snowboardbootsdb',
            name='Size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snowboarddb',
            name='Availability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snowboarddb',
            name='Size',
            field=models.IntegerField(),
        ),
    ]