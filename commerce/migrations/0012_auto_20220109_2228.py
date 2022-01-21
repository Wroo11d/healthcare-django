# Generated by Django 3.2.9 on 2022-01-09 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0011_hospital_hospital_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hospital_category',
            new_name='DoctorCategory',
        ),
        migrations.RenameModel(
            old_name='Doctor_category',
            new_name='HospitalCategory',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Hospital_category',
        ),
        migrations.AddField(
            model_name='hospital',
            name='HospitalCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Hospitals', to='commerce.hospitalcategory'),
        ),
    ]
