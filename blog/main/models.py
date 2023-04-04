from django.db import models

"""
    class Postagem
        -id:int
        -titulo:varchar
        -conteudo:text
        -criado_em:datetime
        -modificado_em:datetime
"""

class Postagem(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    # String representation
    def __str__(self) -> str:
        return self.titulo

    # Sobrescrever no painel admin o nome plural do model 
    class Meta:
        verbose_name_plural = "Postagens"