from django.db import models


class Competence(models.Model):
    CATEGORIES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('outil', 'Outils'),
        ('autre', 'Autres'),
    ]
    nom = models.CharField(max_length=50)
    icone = models.CharField(max_length=100, default='💻')
    niveau = models.IntegerField(default=80, help_text="Niveau de 0 à 100")
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='frontend')
    description = models.CharField(max_length=100, blank=True)
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre', 'nom']
        verbose_name = 'Compétence'
        verbose_name_plural = 'Compétences'

    def __str__(self):
        return self.nom


class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Ex: React, Node.js, MongoDB")
    lien_github = models.URLField(blank=True, verbose_name='Lien GitHub')
    lien_demo = models.URLField(blank=True, verbose_name='Lien Demo')
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    emoji = models.CharField(max_length=5, default='🚀', help_text="Emoji affiché si pas d'image")
    en_vedette = models.BooleanField(default=False, verbose_name='Mettre en avant')
    ordre = models.IntegerField(default=0)
    date_creation = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['ordre', '-date_creation']
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.titre

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',')]


class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_envoi']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"{self.nom} — {self.sujet}"
