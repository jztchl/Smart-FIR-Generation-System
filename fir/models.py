from django.db import models

class FIR(models.Model):
    crime_scene = models.TextField()
    objects_detected = models.JSONField()
    people_identified = models.JSONField()
    extracted_text = models.TextField()
    generated_fir = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FIR - {self.timestamp}"

