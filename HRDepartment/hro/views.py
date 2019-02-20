from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
                                 
from . import models
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from hro.models import Patient


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class DoctorListView(ListView):
    #This create context dict for doctor, to reference it in html file
    context_object_name = 'doctors'

    model =  models.Doctor

class DoctorDetailView(DetailView):
    #This create context dict for doctor, to reference it in html file
    context_object_name = 'doctor_details'
    model = models.Doctor
    template_name  = 'hro/doctor_details.html'

class CreateDoctor(CreateView):
    fields  = ('Doctor_Name','Doctor_Department','Specialization','Sex','Phone_Number','Qualification','Location')
    model = models.Doctor


#Creating Patient class using CreateView
class PatientCreateView(CreateView):
    fields = ("Refer_to_Doctor","Address","Patient_Name","Phone_Number","DOB")
    model = models.Patient

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse('hro:index'))
        
class PatientList(ListView):
    #This create context dict for doctor, to reference it in html file
    context_object_name = 'patient_list'
    model = models.Patient
    template_name  = 'hro/patient_list.html'
    
#Creating Update View 
class PatientUpdateView(UpdateView):
    #These are the fields for updating
    fields = ("Refer_to_Doctor","Address")
    #Here is the var model binding to model name Patient in model.py
    model = models.Patient

class PatientDeleteView(DeleteView):
    model = models.Patient
    context_object_name = 'delete_patient_context'
    success_url = reverse_lazy("hro:list") 

class CreateDepartment(CreateView):
    context_object_name = 'department'
    fields = ('Department_Name','HOD')
    model = models.Department