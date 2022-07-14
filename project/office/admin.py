from django.contrib import admin

# Register your models here.
from office.models import Patient, User, Schedule, Appointment, MedicalFile

admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Appointment)
admin.site.register(MedicalFile)