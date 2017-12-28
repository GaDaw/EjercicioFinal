# Generated by Django 2.0 on 2017-12-28 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20171228_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disputedtournament',
            name='fighters',
            field=models.ManyToManyField(related_name='fighter', to='main.Tournament'),
        ),
        migrations.AlterField(
            model_name='disputedtournament',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='main.Tournament'),
        ),
    ]
