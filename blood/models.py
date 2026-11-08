from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Donar(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='donar')
    phone_number = models.CharField(max_length=20)
    CHOICE_BLOOD = [
    ('A+', 'A Positive (A+)'),
    ('A-', 'A Negative (A-)'),
    ('B+', 'B Positive (B+)'),
    ('B-', 'B Negative (B-)'),
    ('AB+', 'AB Positive (AB+)'),
    ('AB-', 'AB Negative (AB-)'),
    ('O+', 'O Positive (O+)'),
    ('O-', 'O Negative (O-)'),
]
    blood_group = models.CharField(max_length=50,choices=CHOICE_BLOOD,)
    location = models.CharField(max_length=200)
    AVAILAVLE_STATUS = [
        ('availavle','Availalble'),
        ('notavailavle','Notavailavle')
    ]
    available =models.CharField(max_length=50,choices=AVAILAVLE_STATUS)
    last_donation_date = models.DateField(max_length=50)



class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    donar = models.ForeignKey(Donar,on_delete=models.CASCADE,related_name='donar')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    CHOICE_BLOOD = [
    ('A+', 'A Positive (A+)'),
    ('A-', 'A Negative (A-)'),
    ('B+', 'B Positive (B+)'),
    ('B-', 'B Negative (B-)'),
    ('AB+', 'AB Positive (AB+)'),
    ('AB-', 'AB Negative (AB-)'),
    ('O+', 'O Positive (O+)'),
    ('O-', 'O Negative (O-)'),
]
    blood_group = models.CharField(max_length=50,choices=CHOICE_BLOOD,)
    hospital_name = models.CharField(max_length=100)
    bagh_of_blood = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    


