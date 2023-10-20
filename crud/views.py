from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):  # Read
    all_clients = ClientInfo.objects.all()
    return render(request, 'index.html', {'all_clients': all_clients})


def add_client(request):  #
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')

        # print(10*'---',name,email,phone,status)

        client = ClientInfo(name=name, email=email, phone=phone, status=status)
        client.save()
        return redirect('home')

    return render(request, 'index.html')

def delete_client(request, id):  # DELETE

    client = ClientInfo.objects.get(id=id)
    client.delete()
    return redirect('home')

     # return render(request,'index.html')


def edit_client(request, id):  # UPDATE
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')

        # print(10*'---',name,email,phone,status)

        client = ClientInfo.objects.get(id=id)

        client.name = name
        client.email = email
        client.phone = phone
        client.status = status
        client.save()

        return redirect('home')

    else:
        client = ClientInfo.objects.get(id=id)
        context = {
            'client': client,
        }
        return render(request, 'edit.html', context)



