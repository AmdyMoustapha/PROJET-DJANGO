from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def accueil_views(request):
    #===== les differente moyen de 'affiche la template

    return render(request,"accueil.html",{})

    #return redirect('accueil') # ne marche pas

    # template = loader.get_template('accueil.html')
    # return HttpResponse(template.render())