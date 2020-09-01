from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import Registration


def traineeregister(request):

    if request.method == 'POST':
        print('jh')
        form = Registration(request.POST)
        a=form.auto_id


        if form.is_valid():
            print('hiii')

            form.save()
            return redirect('register')
    else:
        form = Registration()
    return render(request,'registration.html',{'form':form})



