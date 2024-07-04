from django.db import models


class Territory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date_of_formation = models.DateField()
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    parking = models.BooleanField(default=True)
    field_child = models.BooleanField(default=True)
    elevator = models.BooleanField(default=True)

    def __str__(self):
        return self.name

