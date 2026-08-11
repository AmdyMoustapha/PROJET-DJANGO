from django import forms
from django.core.exceptions import ValidationError

class InscriptionForm(forms.Form):
    nom_utilisateur = forms.CharField(
        label="Nom d'utilisateur", 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    mot_de_passe = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirmation_mot_de_passe = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    # Validation personnalisée pour l'ensemble du formulaire
    def clean(self):
        cleaned_data = super().clean()
        mdp = cleaned_data.get("mot_de_passe")
        confirmation = cleaned_data.get("confirmation_mot_de_passe")

        if mdp and confirmation and mdp != confirmation:
            raise ValidationError("Les deux mots de passe ne correspondent pas.")
        
        return cleaned_data