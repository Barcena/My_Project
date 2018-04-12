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
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save() #creates the user in the database, saves information
			return redirect('home:home')
	else:
		form=RegistrationForm()

		args = {'form':form} 
		return render(request, 'accounts/reg_form.html', args)

 #decorator
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

















