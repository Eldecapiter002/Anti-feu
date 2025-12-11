from django.db import models

CAUSE_CHOICES = [
    ('electric', 'Courant électrique'),
    ('cooking', 'Cuisson / bois de chauffage'),
    ('arson', 'Incendie criminel'),
    ('other', 'Autre'),
]

class FireIncident(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    cause = models.CharField(max_length=20, choices=CAUSE_CHOICES, default='other')
    houses_burned = models.IntegerField(default=0)
    injured = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cause} - {self.date} {self.time or ''}"

