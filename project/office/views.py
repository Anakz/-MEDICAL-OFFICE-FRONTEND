from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from office.models import Patient, User, Schedule, Appointment, MedicalFile
from office.serializers import PatientSerializer, UserSerializer, ScheduleSerializer, AppointmentSerializer, MedicalFileSerializer

##########

class PatientViewSet(ModelViewSet):

    #queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.all()

##########

class UserViewSet(ModelViewSet):


    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

##########

class ScheduleViewSet(ModelViewSet):


    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()

##########

class AppointmentViewSet(ModelViewSet):


    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.all()

##########
class MedicalFileViewSet(ModelViewSet):

    serializer_class = MedicalFileSerializer

    def get_queryset(self):
        return MedicalFile.objects.all()

