from django import forms
from home.models import Company



class CompanyForm(forms.ModelForm):

    class Meta: 
        model = Company
        fields = (
            'facebook_name',
            'amount',
            'duration',
     
        )
    def save(self, commit=True):#save in database
         company = super(CompanyForm,self).save(commit=False)
         company.amount = self.cleaned_data['amount']
         company.duration = self.cleaned_data['duration']
         

         if commit:
            company.save()

         return company