from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.JSONField()  # JSONField for structured data

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.date}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
