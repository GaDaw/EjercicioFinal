# Generated by Django 2.0 on 2017-12-27 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171227_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disputedtournament',
            name='id',
        ),
        migrations.AlterField(
            model_name='disputedtournament',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Tournament'),
        ),
    ]