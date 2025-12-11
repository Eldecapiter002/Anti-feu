from django.db import models

CAUSE_CHOICES = [
    ('electric', 'Courant électrique'),
    ('cooking', 'Cuisson / bois de chauffage'),
    ('arson', 'Incendie criminel'),
    ('other', 'Autre'),
]

class FireIncident(models.Model):
    title = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100, blank=True)
    avenue = models.CharField(max_length=200, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    cause = models.CharField(max_length=20, choices=CAUSE_CHOICES, default='other')
    houses_burned = models.IntegerField(default=0)
    injured = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commune} - {self.date} {self.time or ''}"

class IncidentPhoto(models.Model):
    incident = models.ForeignKey(FireIncident, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='incidents/%Y/%m/%d/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Photo {self.id} - {self.incident}"
