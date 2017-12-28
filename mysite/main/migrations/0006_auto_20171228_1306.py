# Generated by Django 2.0 on 2017-12-28 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171228_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='Nombre', serialize=False, to='main.Fighter'),
        ),
    ]
