from django.contrib import admin
from .models import Projet, Competence, Message


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['titre', 'technologies', 'en_vedette', 'ordre', 'date_creation']
    list_editable = ['en_vedette', 'ordre']
    list_filter = ['en_vedette']
    search_fields = ['titre', 'description']


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'icone', 'categorie', 'niveau', 'ordre']
    list_editable = ['niveau', 'ordre']
    list_filter = ['categorie']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'sujet', 'date_envoi', 'lu']
    list_editable = ['lu']
    list_filter = ['lu']
    readonly_fields = ['nom', 'email', 'sujet', 'message', 'date_envoi']
