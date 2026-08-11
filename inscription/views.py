from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InscriptionForm

# Create your views here.

# def inscrire_utilisateur(request):
#     if request.method == 'POST':
#         form = InscriptionForm(request.POST)
#         if form.is_valid():
#             # Récupération des données validées
#             nom = form.cleaned_data['nom_utilisateur']
#             email = form.cleaned_data['email']
#             mdp = form.cleaned_data['mot_de_passe']
            
#             # Action personnalisée (ex: appeler une API externe ou envoyer un e-mail)
#             # ...
            
#             messages.success(request, f"Inscription réussie pour {nom} !")
#             return redirect('accueil')
#     else:
#         form = InscriptionForm()
        
#     return render(request, 'inscription.html', {'form': form})

def inscription_view(request):
    return render(request,"inscription.html",{})