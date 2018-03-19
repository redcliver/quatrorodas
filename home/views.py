from django.shortcuts import render
from django.contrib.auth import authenticate
from ordem.models import ordens

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        os = ordens.objects.filter(estado=2).count()
        msg = "Ola, temos "+str(os)+" ordens em aberto."
        return render(request, 'home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'erro.html', {'title':'Erro'})