# Generated by Django 3.2.9 on 2022-01-09 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0015_auto_20220109_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='DoctorCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctors', to='commerce.doctorcategory'),
        ),
    ]
