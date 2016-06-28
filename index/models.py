from django.db import models


class Customer(models.Model):
    fName = models.CharField(max_length=250)
    lName = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)

    def __str__(self):
        return self.fName + " " + self.lName + " - " + self.occupation