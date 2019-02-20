from django.db import models
from django.urls import reverse



class Department(models.Model):
    Department_Name = models.CharField(max_length=200)
    HOD = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.Department_Name

    def get_absolute_url (self):
        return reverse('hro:detail', kwargs={'pk':self.pk})

    # class Meta:
    #     models = Department # This should be "model" not "models".
    #     fields = ('Department_Name',)

# Create your models here.
class Doctor(models.Model):
    Doctor_Name = models.CharField(max_length=150, default='')
    Employed_On = models.DateTimeField(auto_now=True)
    Doctor_Department = models.ForeignKey(Department, related_name='department', on_delete=models.PROTECT, default='') 
    Specialization = models.CharField(max_length=150, default='')
    Sex = models.CharField(max_length=7, default='')
    Phone_Number = models.CharField(max_length=12, unique=True, default='')
    Address = models.CharField(max_length=100, default='')
    Qualification = models.CharField(max_length=256, default='')
    Location = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.Doctor_Name

class Patient(models.Model):
    Patient_Name = models.CharField(max_length=256, default='')
    DOB = models.DateField()
    Phone_Number = models.CharField(max_length=13,unique=True,)
    Age = models.CharField(max_length=200, default='')
    Address = models.CharField(max_length=256)
    Refer_to_Doctor = models.ForeignKey(Doctor,related_name='patientsRefName', on_delete=models.PROTECT, unique=False)
    Symptom = models.CharField(max_length=256, default='')
    Date_Reported_Sick = models.DateField()
    
    def __str__(self):
        return self.Patient_Name

    def get_absolute_url(self):
        return reverse("hro:detail", kwargs={'pk':self.pk})

# class Nurse(models.Model):
#     Nurse_Name = models.CharField(max_length=200)
#     Phone_Number = models.IntegerField(max_length=14)
#     Patient_Assigned = models.ForeignKey(Patient, related_name='patient_ref', on_delete=models.PROTECT)
