from rest_framework import serializers
from .models import FireIncident

class FireIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireIncident
        fields = '__all__'

    def validate(self, data):
        # exiger latitude et longitude lors de la création (si absent -> erreur)
        if self.instance is None:  # création
            lat = data.get('latitude')
            lng = data.get('longitude')
            if lat is None or lng is None:
                raise serializers.ValidationError("Latitude et longitude sont requises. Sélectionne un point sur la carte.")
        return data
