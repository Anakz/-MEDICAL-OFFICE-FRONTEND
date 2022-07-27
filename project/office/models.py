# from asyncio.windows_events import NULL
from datetime import datetime
from django.db import models

from django.core.validators import MinValueValidator
# Create your models here.

class Patient(models.Model):

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

    firstName = models.fields.CharField(max_length=20, null=False)
    lastName = models.fields.CharField(max_length=20, null=False)
    cin = models.fields.CharField(max_length=20, null=False)
    phone = models.fields.CharField(max_length=20, null=False)
    email = models.fields.EmailField(max_length=100, null=False)
    password = models.fields.CharField(max_length=100, null=False)
    address = models.fields.CharField(max_length=500, null=False)
    gender = models.fields.CharField(max_length=10, null=True, default=None)
    dateBirth = models.fields.DateField(null=False)
    isDelete = models.fields.DateTimeField(null=True, default=None, blank=True)


class User(models.Model):

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    
    firstName = models.fields.CharField(max_length=20, null=False)
    lastName = models.fields.CharField(max_length=20, null=False)
    cin = models.fields.CharField(max_length=20, null=False)
    phone = models.fields.CharField(max_length=20, null=False)
    email = models.fields.EmailField(max_length=100, null=False)
    password = models.fields.CharField(max_length=100, null=False)
    address = models.fields.CharField(max_length=500, null=False)
    salary = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    beginDate = models.fields.DateField(null=True, blank=True, default=None)
    endDate = models.fields.DateField(null=True, blank=True, default=None)
    role = models.fields.CharField(max_length=20, null=False)
    isDelete = models.fields.DateTimeField(null=True, default=None, blank=True)

class Schedule(models.Model):

    def __str__(self):
        return f'{self.date} | {self.user} | {self.availability}'

    date = models.fields.DateTimeField(null=True, blank=True)
    availability = models.fields.BooleanField(default=False)
    isDelete = models.fields.DateTimeField(null=True, default=None, blank=True)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class Appointment(models.Model):

    def __str__(self):
        return f' {self.patient} {self.date}'

    date = models.fields.DateTimeField(null=True, blank=True)
    paymentStatus = models.fields.BooleanField(default=False, null=False)
    price = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    totalPaid = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=False)
    reason = models.fields.CharField(max_length=1000, null=False)
    prescription = models.fields.CharField(max_length=2000, null=True, blank=True)
    isDelete = models.fields.DateTimeField(null=True, default=None, blank=True)

    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class MedicalFile(models.Model):

    def __str__(self):
        return f'{self.patient} {self.date}'

    date = models.fields.DateTimeField(null=True, blank=True)
    bloodGroup = models.fields.CharField(max_length=5, null=False)
    height = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=False)
    weight = models.fields.FloatField(
        validators=[MinValueValidator(0)],
        null=False)
    allergy = models.fields.CharField(max_length=2000, null=True, blank=True)
    vaccination = models.fields.CharField(max_length=2000, null=False)
    healthInsurance = models.fields.CharField(max_length=500, null=False)
    isDelete = models.fields.DateTimeField(null=True, default=None, blank=True)

    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)

