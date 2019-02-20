from django.contrib import admin
from hro.models import Doctor, Patient, Department
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Department)
