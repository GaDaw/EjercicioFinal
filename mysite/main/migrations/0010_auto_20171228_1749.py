# Generated by Django 2.0 on 2017-12-28 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20171228_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disputedtournament',
            name='fighters',
            field=models.ManyToManyField(to='main.Fighter'),
        ),
        migrations.AlterField(
            model_name='disputedtournament',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='+', serialize=False, to='main.Tournament'),
        ),
    ]
