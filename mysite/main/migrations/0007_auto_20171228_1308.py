# Generated by Django 2.0 on 2017-12-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171228_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
    ]
