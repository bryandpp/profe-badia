from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .models import Operaciones, Salario, Deudas
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.timezone import now
from .util import DineroActual
# Create your views here.

@login_required
def index(request):
    # notify.send(request.user, recipient=request.user, verb='The items  have been deleted by {}'.format(request.user.username), level='info')
    if request.user is not None:
        date_search = ""
        if request.POST:
            date = request.POST.get("date") #para capturar los parámetros post o get Se debe poner al final get("NombreDelInput")
            tipo = request.POST.get('tipo')
            date_split = date.split('-')


            if tipo == '2':
               op = Operaciones.objects.filter(fecha_operacion__month=date_split[1])
               date_search = 'Mes: {0}'.format(date_split[1])
            elif tipo == '3':
               op = Operaciones.objects.filter(fecha_operacion__year=date_split[0])
               date_search = 'Año   : {0}'.format(date_split[0])
            else:
                op = Operaciones.objects.filter(fecha_operacion=date)
                date_search = date

        else:
            date = now().date().strftime('%Y-%m-%d')
            op = Operaciones.objects.filter(fecha_operacion=date)
            date_search = now().date().strftime('%Y-%m-%d')


        context = {
            'date': date,
            'date_search': date_search,
            'operaciones': op,
            'salario': Salario.objects.last().cantidad(),
            'dineroActual': DineroActual(),
        }
        return render(request, '../templates/economy/index.html', context)
    else:
        return HttpResponse('Not user found')

