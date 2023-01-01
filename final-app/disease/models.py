from django.db import models

class Image(models.Model):
    image=models.ImageField(upload_to='images/')

class Result(models.Model):
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    predicted_label=models.CharField(max_length=200)
    normal=models.FloatField(blank=True, null=True)
    other_abnormalities=models.FloatField(blank=True, null=True)
    pathological_myopia=models.FloatField(blank=True, null=True) 
    hypertension=models.FloatField(blank=True, null=True)
    glaucoma=models.FloatField(blank=True, null=True)
    diabetes=models.FloatField(blank=True, null=True)
    cataract=models.FloatField(blank=True, null=True)
    age_related_macular_degeneration=models.FloatField(blank=True, null=True)
    
