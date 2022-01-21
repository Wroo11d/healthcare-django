import datetime

from ninja import Schema
from pydantic import UUID4
from django.contrib.auth import get_user_model

User=get_user_model()


class doctorIn(Schema):
    image : str
    name : str
    description : str
    open_time : datetime.time
    close_time : datetime.time
    days : str
    location : str
    #Doctor_category :

class doctorOut(Schema):
    id : UUID4
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str


class update_doctor(Schema):
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str

#########################################

class DcategoryIn(Schema):
    type : str



class DcategoryOut(Schema):
    id : UUID4
    type: str
    Doctors : list[doctorOut]


class update_Dcategory(Schema):
    type: str

#########################################

class DoctorTypeIn(Schema):
    type : str



class DoctorTypeOut(Schema):
    id : UUID4
    type: str
    Doctors : list[doctorOut]


class update_DoctorType(Schema):
    type: str



#######################################
class hospitalIn(Schema):
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str




class hospitalOut(Schema):
    id:UUID4
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str
    # Hospital_category :


class update_hospital(Schema):
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str
    # Hospital_category :


#############################################

class HcategoryIn(Schema):
    type: str


class HcategoryOut(Schema):
    id: UUID4
    type: str
    Hospitals: list[hospitalOut]

class update_Hcategory(Schema):
    type: str


#############################################

class HospitalTypeIn(Schema):
    type: str


class HospitalTypeOut(Schema):
    id: UUID4
    type: str
    Hospitals: list[hospitalOut]

class update_HospitalType(Schema):
    type: str


