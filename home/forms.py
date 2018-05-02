
from django import forms
from home.models import Post
from home.models import Company

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget = forms.TextInput(
    	attrs={
    		'class':'form-control',
    		'placeholder':'Write a post ... '
    	}

    	))


    class Meta:
        model = Post
        fields = ('post',)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
