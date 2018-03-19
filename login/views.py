from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

def erro(request):
    return render(request, 'erro.html', {'title':'Erro'})