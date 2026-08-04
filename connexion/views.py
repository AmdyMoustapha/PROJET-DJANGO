from django.shortcuts import render, redirect

# Create your views here.
def connexion_view(request):
    # if request.user.is_authenticated:
    #     return redirect("accueil")

    # if request.method == "POST":
    #     nom = request.POST.get("nom")
    #     mot_de_passe = request.POST.get("mot_de_passe")

    #     user = authenticate(request, username=nom, password=mot_de_passe)
    #     if user is not None:
    #         login(request, user)

    #         # Correction de la faille de redirection ouverte (Open Redirection)
    #         next_url = request.GET.get("next")
    #         if next_url and url_has_allowed_host_and_scheme(
    #             url=next_url, allowed_hosts={request.get_host()}
    #         ):
    #             return redirect(next_url)
    #         return redirect("accueil")
    #     else:
    #         messages.error(request, "Identifiant ou mot de passe incorrect.")
    # return render(request, "connexion.html")
    return render(request,"connexion.html",{})