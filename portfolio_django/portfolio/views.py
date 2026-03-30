from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Projet, Competence
from .forms import ContactForm


def home(request):
    projets = Projet.objects.all()
    competences_frontend = Competence.objects.filter(categorie='frontend')
    competences_backend = Competence.objects.filter(categorie='backend')
    competences_outils = Competence.objects.filter(categorie='outil')
    competences_autres = Competence.objects.filter(categorie='autre')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            # Envoi email (affiché dans la console en mode DEBUG)
            try:
                send_mail(
                    subject=f"[Portfolio] {msg.sujet}",
                    message=f"De: {msg.nom} <{msg.email}>\n\n{msg.message}",
                    from_email=msg.email,
                    recipient_list=['alex@example.com'],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, '✅ Message envoyé ! Je vous répondrai bientôt.')
            return redirect('home')
        else:
            messages.error(request, '❌ Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = ContactForm()

    context = {
        'projets': projets,
        'competences_frontend': competences_frontend,
        'competences_backend': competences_backend,
        'competences_outils': competences_outils,
        'competences_autres': competences_autres,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)
