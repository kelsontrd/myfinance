from django.db import models

class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True , verbose_name='atualizado em')

    def __str__(self):
        return f"Criado em : {self.created_at}, Updated at: {self.updated_at}"
    class Meta:
        abstract = True
        ordering = ['-created_at']
        verbose_name = 'Carimbo de Tempo'
        verbose_name_plural = 'Carimbos de Tempo'