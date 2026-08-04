from django.shortcuts import render

# Create your views here.
def inscription_view(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():  
            data = form.cleaned_data
            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=data["email"],
                        email=data["email"],
                        password=data["mot_de_passe"],
                        first_name=data["prenom"],
                        last_name=data["nom"],
                    )
                    # Assurez-vous que le modèle 'Utilisateur' existe
                    Utilisateur.objects.create(
                        user=user,
                        telephone=data["telephone"],
                        adresse=data["adresse"],
                    )
                messages.success(
                    request, "Votre compte et votre profil ont été créés !"
                )
                return redirect("connexion")

            except Exception as e:
                form.add_error(
                    None, f"Une erreur est survenue lors de l'inscription : {e}"
                )
    else:
        form = InscriptionForm()
    return render(request, "register.html", {"form": form})