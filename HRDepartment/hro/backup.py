# from django.db import models
# from django.urls import reverse



# # Create your models here.
# class Doctor(models.Model):
#     Doctor_Name = models.CharField(max_length=256) 
#     Department = models.CharField(max_length=256)
#     Qualification = models.CharField(max_length=256)
#     Location = models.CharField(max_length=256)

#     def __str__(self):
#         return self.Doctor_Name

# class Patient(models.Model):
#     Patient_Name = models.CharField(max_length=256)
#     DOB = models.DateField()
#     Phone_Number = models.CharField(max_length=13)
#     Address = models.CharField(max_length=256)
#     Refer_to_Doctor = models.ForeignKey(Doctor,related_name='patientsRefName', on_delete=models.PROTECT)
#     #Refer_Doctor = models.

#     def __str__(self):
#         return self.Patient_Name


#     def get_absolute_url(self):
#         return reverse("hro:detail", kwargs={'pk':self.pk})

# class Nurse(models.Model):
#     Nurse_Name = models.CharField(max_length=200)
#     Phone_Number = models.IntegerField(max_length=14)
#     Patient_Assigned = models.ForeignKey(Patient, related_name='patient_ref', on_delete=models.PROTECT)

#     def __str__(self):
#         return self.Nurse_Name

#     def get_absolute_url (self):
#         return reverse('hro:detail', kwargs={'pk':self.pk})






#NAV