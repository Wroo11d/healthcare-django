# Generated by Django 3.2.9 on 2022-01-19 07:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0016_doctor_doctorcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HospitalType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='DoctorType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctors', to='commerce.doctortype'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='HospitalType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Hospitals', to='commerce.hospitaltype'),
        ),
    ]
