from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .models import Department, Order


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return redirect('new_page')
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def new_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        department_id = request.POST['department']
        purpose = request.POST['purpose']
        materials_provide = request.POST.getlist('materials_provide')
        order = Order.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            department_id=department_id,
            purpose=purpose,
            materials_provide=", ".join(materials_provide)
        )
        return render(request, 'success.html', {'order': order})

    departments = Department.objects.all()
    return render(request, 'new_page.html', {'departments': departments})

def success(request):
    success(request)
    return render(request,'success.html')

def logout(request):
    logout(request)
    return redirect('home')

from django.core import serializers
#this function is to return a json to frontend 
def departments(request):
    departments = Department.objects.all()
    departments_data = serializers.serialize('python', departments)
    departments_list = [item['fields'] for item in departments_data]
    print('departments_list',departments_list)
    return JsonResponse(departments_list, safe=False)


