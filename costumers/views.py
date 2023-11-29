from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from django.urls import reverse
import costumers
from costumers.forms import CostumersForm

def login(request):
    if request.method == 'POST':
        form = CostumersForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  
            return HttpResponseRedirect(reverse(costumers.costumer))
        
    else:
        pass
    
