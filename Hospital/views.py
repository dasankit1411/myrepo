from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from Hospital.models import *
# Create your views here.
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    appointments=Appointment.objects.all()
    d=0;
    p=0;
    a=0;
    for i in doctors:
        d=d+1
    for i in patients:
        p=p+1
    for i in appointments:
        a=a+1
    d1={'d':d,'p':p,'a':a}
    return render(request,'hospital/index.html',d1)

def Login(request):
    error=''
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'hospital/login.html',d)

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Aboutus(request):
    return render(request,'hospital/about.html')

def Contact(request):
    return render(request,'hospital/contact.html')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'hospital/view_doctor.html',d)

def Add_doctor(request):
    error=''
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['specialization']
        try:
            Doctor.objects.create(name=n,mobile=c,specialization=sp)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'hospital/add_doctor.html',d)

def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    p={'pat':pat}
    return render(request,'hospital/view_patient.html',p)

def Delete_patient(request,sid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=sid)
    patient.delete()
    return redirect('view_patient')


def Add_patient(request):
    error=''
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        nm=request.POST['name']
        gn=request.POST['gender']
        ct=request.POST['contact']
        add=request.POST['address']
        try:
            Patient.objects.create(name=nm,gender=gn,mobile=ct,address=add)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'hospital/add_patient.html',d)


def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.all()
    p={'appointment':appointment}
    return render(request,'hospital/view_appointment.html',p)

def Delete_appointment(request,sid):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.get(id=sid)
    appointment.delete()
    return redirect('view_appointment')


def Add_appointment(request):
    error=''
    if not request.user.is_staff:
        return redirect("login")
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method=='POST':
        dn=request.POST['doctor']
        pn=request.POST['patient']
        d1=request.POST['date']
        t1=request.POST['time']
        doctor=Doctor.objects.filter(name=dn).first()
        patient=Patient.objects.filter(name=pn).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t1)
            error='no'
        except:
            error='yes'
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'hospital/add_appointment.html',d)
