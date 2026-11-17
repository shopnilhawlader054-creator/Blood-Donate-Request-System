from django.shortcuts import render,redirect,get_object_or_404
from .models import Donar,Patient
from .forms import Registerform,Donorform,Patiendform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate,logout

# Create your views here.


def home(request):
    print('hitting sucess')
    return render(request,'donor_list.html')



def user_all_donar_request(request,pk):
    patient = Patient.objects.filter(user=request.user)
    context = {
        'patient':patient
    }
    return render(request,'my_request.html',context)
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
      form = Donorform()
    return render(request,'donor_form.html',{'form':form})


def donor_request(request,pk):
    if request.method =='POST':
        form = Patiendform(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.donar = pk
            data.save()
            return redirect('home')
    else:
        form = Patiendform()
    return render(request,'blood_request_form.html',{'form':form})


def view_donor_profile(request):
    donor = get_object_or_404(Donar,user=request.user)
    print('view donor')
    return render(request,'profile.html',{'donor':donor}) 


  
