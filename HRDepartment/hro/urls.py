from django.conf.urls import url, include
from hro import views

app_name = 'hro'

urlpatterns = [

    url(r'^$', views.DoctorListView.as_view(), name='list'),
     #rl(r'^$', views.LogoutPage.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.DoctorDetailView.as_view(), name='detail'),
    url(r'^patient_list/$', views.PatientList.as_view(), name='patient_list'),
    url(r'^create_patient/$', views.PatientCreateView.as_view(), name='create_patient'),
    url(r'^update_patient/(?P<pk>\d+)/$', views.PatientUpdateView.as_view(), name='update_patient'),
    url(r'^delete_patient/(?P<pk>\d+)/$', views.PatientDeleteView.as_view(), name='delete_doctor'),
    #url(r'^delete_patient/(?P<pk>\d+)/$', views.PatientDeleteView.as_view(), name='delete_doctor'),
    url(r'^create_doctor/$', views.CreateDoctor.as_view(), name='create_doctor'),
    url(r'^create_department/$', views.CreateDepartment.as_view(), name='create_department'),
]