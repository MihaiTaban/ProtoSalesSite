# Generated by Django 3.1.6 on 2021-02-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skibootsdb',
            name='Availability',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='skibootsdb',
            name='Size',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='skidb',
            name='Availability',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='skidb',
            name='Size',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='snowboardbootsdb',
            name='Availability',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='snowboardbootsdb',
            name='Size',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='snowboarddb',
            name='Availability',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='snowboarddb',
            name='Size',
            field=models.IntegerField(verbose_name=200),
        ),
    ]
