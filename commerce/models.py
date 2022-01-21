import uuid

from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

from config.utils.models import Entity

#User = get_user_model()


class Doctor(Entity):
    image = models.ImageField('image', upload_to='Doctors/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    description = models.TextField('description', blank=True, null=True)
    open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    days = models.TextField('days', null=True, blank=True)
    location = models.TextField('location', null=True, blank=True)
    DoctorType = models.ForeignKey('DoctorType', related_name='Doctors', null=True, blank=True, on_delete=models.CASCADE)
    DoctorCategory = models.ForeignKey('DoctorCategory', related_name='Doctors', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hospital(Entity):
    image = models.ImageField('image', upload_to='Hospitals/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    location = models.TextField('location', null=True, blank=True)
    time = models.CharField('time', null=True, blank=True, max_length=255)
    """open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)"""
    days = models.TextField('days', null=True, blank=True)
    beds = models.IntegerField('beds', null=True, blank=True)
    description = models.TextField('description', blank=True, null=True)
    HospitalType = models.ForeignKey('HospitalType', related_name='Hospitals', null=True, blank=True, on_delete=models.CASCADE)
    HospitalCategory = models.ForeignKey('HospitalCategory', related_name='Hospitals', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class DoctorCategory(Entity):
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type


class HospitalCategory(Entity):
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type


class HospitalType(Entity):
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type


class DoctorType(Entity):
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type
