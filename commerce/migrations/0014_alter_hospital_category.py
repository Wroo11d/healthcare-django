# Generated by Django 3.2.9 on 2022-01-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0013_auto_20220109_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospitals', to='commerce.category'),
        ),
    ]