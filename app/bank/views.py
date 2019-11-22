from django.shortcuts import render
from django.http import HttpResponse
from bank.models import Branch,Customer,Account,Product

# Create your views here.
def read(request):
    query_data = Branch.objects.all()
    return HttpResponse(query_data.values())