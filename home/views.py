from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response  import Response
import datetime
from home.forms import CompanyForm
from .models import Company
from .serializers import CompanySerializer

def register(request):
    if request.method=='POST': #POST method means user is sendding data to webbserver
            form = CompanyForm(request.POST)
            if form.is_valid():
                form.save() #creates the user in the database, saves information
                return redirect('home:res')
    else:
            form=CompanyForm()

            args = {'form':form}
            return render(request, 'home/home.html' , args)


class CompanyListView(ListView):
    model = Company
    paginate_by = 10  # if pagination is desired
    context_object_name = "company_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context



class CompanyDetail(APIView):

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def view_company(request, pk=None):
    company = Company.objects.all()
    args = {'company': company }
    return render(request, 'simulator/simulator.html', args)
