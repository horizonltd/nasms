from django.views.generic import TemplateView
from hro.models import Patient
from django.http import HttpResponse, HttpResponseRedirect


# def display(request, self):
#   return HttpResponseRedirect('patient_list.html', {'query_results': self.models.Patient.objects.all()})


# def MyView(request, self):
#     query_results = self.Patient.objects.all()
#     ...
#    # query_results = Patient.objects.all()


class HomePage(TemplateView):
    template_name = 'index.html'
class Advice(TemplateView):
    template_name = 'advice.html'

# This view are from templates folder
class ThanksPage(TemplateView):
    template_name = "thanks.html"


class TestPage(TemplateView):
    template_name = "test.html"
