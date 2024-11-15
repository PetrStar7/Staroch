from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Tablet(models.Model):
    total_tablets = models.PositiveIntegerField(default=30)  # Celkový počet dostupných tabletů
    
    def __str__(self):
        return f"Tablety: {self.total_tablets}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Uživatel, který rezervaci vytvořil
    den = models.CharField(max_length=10, choices=[('Po', 'Pondělí'), ('Út', 'Úterý'), ('St', 'Středa'),
                                                   ('Čt', 'Čtvrtek'), ('Pá', 'Pátek')])  # Den rezervace
    hodina = models.PositiveIntegerField()  # Hodina od 1 do 8
    pocet = models.PositiveIntegerField()  # Počet rezervovaných tabletů
    datum = models.DateField(auto_now_add=True)  # Datum vytvoření rezervace

    def __str__(self):
        return f"{self.user.username} - {self.den}, Hodina: {self.hodina}, Tablety: {self.pocet}"
