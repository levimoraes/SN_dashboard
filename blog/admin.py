from django.contrib import admin
from .models import Post, Candidato

admin.site.register(Candidato)
admin.site.register(Post)