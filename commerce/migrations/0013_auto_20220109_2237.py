# Generated by Django 3.2.9 on 2022-01-09 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0012_auto_20220109_2228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HospitalCategory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='HospitalCategory',
            new_name='Category',
        ),
    ]
