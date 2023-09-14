from django.db import models

class School(models.Model):
    REGION_OPTIONS = (
        ('Accra', 'Accra'),
        ('Ashanti', 'Ashanti'),
        ('Eastern', 'Eastern'),
        ('Central', 'Central'),
        ('Volta', 'Volta'),
        ('Northern', 'Northern'),
        ('Upper East', 'Upper East'),
        ('Upper West', 'Upper West'),
        ('Western', 'Western'),
        ('Western North', 'Western North'),
        ('Bono', 'Bono'),
        ('Bono East', 'Bono East'),
        ('Ahafo', 'Ahafo'),
        ('Oti', 'Oti'),
        ('Savannah', 'Savannah')
    )

    name = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    region =  models.CharField(max_length=200, choices=REGION_OPTIONS)

    def __str__(self):
        return self.name
