from django.contrib import admin
from .models import Postagem

# Registrar a Postagem no painel de admin
admin.site.register(Postagem)