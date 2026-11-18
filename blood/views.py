from django.shortcuts import render,redirect,get_object_or_404
from .models import Donar,Patient
from .forms import Registerform,Donorform,Patiendform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate,logout

# Create your views here.


def home(request):
    donor = Donar.objects.all()
    return render(request,'donor_list.html',{'donors':donor})



def user_all_donar_request(request,pk):
    patient = Patient.objects.filter(user=request.user)
    context = {
        'patient':patient
    }
    return render(request,'my_request.html',context)
def donor_detals(request,pk):
    donor = get_object_or_404(Donar,pk=pk)
    return render(request,'donor_details.html',{'donor':donor})

def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = Registerform()
        
    return render(request, 'acount/register.html', )
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        print('hitting ')
        if form.is_valid():
                user =form.get_user()
                print('fainaly')
                auth_login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
          

    return render(request,'acount/login.html',{'form':form})

def creat_donor(request):
    if request.method =='POST':
        form = Donorform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
      form = None
    return render(request,'donor_form.html',{'donor':form})


def donor_request(request,pk):
    if request.method =='POST':
        form = Patiendform(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.donar_id = pk
            data.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = None
    return render(request,'blood_request_form.html',{'form':form})


def view_donor_profile(request):
    donor = get_object_or_404(Donar,user=request.user)
    print('view donor')
    return render(request,'profile.html',{'donor':donor}) 



def user_logout(request):
    logout(request)
    return redirect('login')

def edit_donor_aocunt(request,pk):
    donor = get_object_or_404(Donar,pk=pk)
    if request.method == 'POST':
        # ফর্ম থেকে নতুন ডেটাগুলো নিয়ে ডোনার অবজেক্টে অ্যাসাইন করা
        donor.name = request.POST.get('name')
        donor.phone_number = request.POST.get('phone_number')
        donor.blood_group = request.POST.get('blood_group')
        donor.location = request.POST.get('location')
        donor.available = request.POST.get('available')
        
        last_date = request.POST.get('last_donation_date')
        if last_date:
            donor.last_donation_date = last_date
        
        donor.save()
        return redirect('view_donor_profile')
  
    return render(request,'donor_form.html',{'donor':donor})

def delete_donar_acount(request,pk):
    donor = get_object_or_404(Donar,pk=pk)
    donor.delete()

def all_petient(request):
    donor = get_object_or_404(Donar,user=request.user)
    patient = Patient.objects.filter(donar=donor, status__in=['Pending', 'Accepted'])
    return render(request,'blood_request.html',{'patients':patient})
def petient_detals(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    donor = get_object_or_404(Donar,user=request.user)
    if request.method =='POST':
        status= request.POST.get('status')
        if status == 'Accepted':
            patient.status = status
            patient.save()
            donor.available='notavailavle'
            donor.save()
            patients= Patient.objects.filter(status='Pending')
            patients.status = 'Committed'
            return redirect('all_petient')
        else:
             patient.status = status
             patient.save()
             return redirect('all_petient')
    return render(request,'blood_details.html',{'patient':patient})



def my_request(request):
    patient = Patient.objects.filter(user=request.user)
    return render(request,'my_request.html',{'patients':patient})


def edit_my_request(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    if request.method =='POST':
        patient.name = request.POST.get('patient_name')
        patient.status = request.POST.get('status',patient.status)
        patient.blood_group = request.POST.get('blood_group')
        patient.hospital_name = request.POST.get('hospital_name')
        patient.bagh_of_blood = request.POST.get('bagh_of_blood')
        patient.contact_number = request.POST.get('contact_number')
        patient.save()
        return redirect('my_request')
    return render(request,'blood_request_form.html',{'patient':patient})

def delet_blood_request(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    patient.delete()
    return redirect('my_request')

def filter_donor(request):
    donor = Donar.objects.all()
    name = request.GET.get('name')
    location = request.GET.get('location')
    number = request.GET.get('phone')
    blood_group = request.GET.get('blood_group')
    if donor:
        donor = donor.filter(name=name)
    if location:
        donor = donor.filter(location = location)
    if number:
        donor = donor.filter(phone_number = number)
    if blood_group:
        donor = donor.filter(blood_group = blood_group)
    return render(request,'donor_list.html',{'donors':donor})
    
  
