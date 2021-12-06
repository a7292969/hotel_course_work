from django.db import models


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + " " + str(self.price)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.name + " - " + self.text
