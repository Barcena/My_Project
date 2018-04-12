# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from accounts.forms import (
	RegistrationForm, 
	EditProfileForm
) #Django user creation form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import B2cRegisterForm
# Create your views here.
# here comes all de logic 
'''def home (request):
	#return render(request, 'accounts/login.html')

	#querys
	numbers =[1,2,3,4,5]
	name='Carlos Bárcena

	args={'myName':name, 'numbers':numbers} # dictionary object
	return render(request,'accounts/home.html', args)'''

def register(request):
	if request.method=='POST': #POST method means user is sendding data to webbserver
		form = B2cRegisterForm(request.POST)
		if form.is_valid():
			form.save() #creates the user in the database, saves information
			return redirect('home:home')
	else:
		form=B2cRegisterForm()

		args = {'form':form} 
		return render(request, 'business/reg_b2c.html', args)

 #decorator
def view_b2c_profile(request, pk=None):
    if pk:
        business = User.objects.get(pk=pk)
    else:
        business = request.user
    args = {'business': business}
    return render(request, 'business/b2c_profile.html', args)

def edit_b2c_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)



