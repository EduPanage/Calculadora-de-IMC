from django.db import models

class IMC(models.Model):
    peso = models.FloatField()
    altura = models.FloatField()
    imc = models.FloatField()
    classificacao = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.imc:.2f} - {self.classificacao}"