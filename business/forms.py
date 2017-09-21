from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import B2cProfile

class B2cRegisterForm(forms.ModelForm):
	email=forms.EmailField(required=True)

	class Meta: 
		model = B2cProfile
		fields = (
			
			'business_name',
			'description',
			'phone',
			'email',
			'apertura',
			'cierre'
		)

	def save(self, commit=True):#save in database
		 b2c = super(B2cRegisterForm,self).save(commit=False)
		 
		 b2c.business_name = self.cleaned_data['business_name']
		 b2c.description = self.cleaned_data['description']
		 b2c.phone = self.cleaned_data['phone']
		 b2c.email = self.cleaned_data['email']
		 b2c.cierre = self.cleaned_data['cierre']
		 b2c.apertura = self.cleaned_data['apertura']
		 if commit:
		 	b2c.save()

		 return b2c

class EditB2cProfileForm(UserChangeForm):
	
	class Meta: # exlude fields in a model
		model = B2cProfile
		fields = (
			'description',
			'business_name',
			'phone',
			)