from django.shortcuts import render
from .models import Donar,Patient

# Create your views here.


def home(request):
    print('hitting sucess')
    return render(request,'blood_request.html')

def user_all_donar_request(request,pk):
    patient = Patient.objects.filter(user=request.user)
    context = {
        'patient':patient
    }
    return render(request,'my_request.html',context)
