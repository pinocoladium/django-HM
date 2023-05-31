from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f'{self.name} {self.description}'

class Measurement(models.Model):
    sensor = models.ForeignKey("Sensor", on_delete=models.CASCADE, related_name='Measurements')
    temperature = models.FloatField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.sensor} {self.temperature}'
    