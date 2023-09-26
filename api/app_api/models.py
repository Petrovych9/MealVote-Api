from django.db import models


# Create your models here.
class Restaurant(models.Model):
    """
        Represents a restaurant.

        Fields:
        - `name` (CharField): The name of the restaurant (maximum length: 255 characters).
        - `address` (TextField): The address of the restaurant.

        Methods:
        - `__str__()`: Returns the name of the restaurant as a string.
        """
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    """
       Represents a menu for a specific restaurant on a particular date.

       Fields:
       - `restaurant` (ForeignKey to Restaurant): The restaurant to which this menu belongs.
       - `date` (DateField): The date on which the menu is available.
       - `items` (JSONField): A field for storing structured data related to menu items.

       Methods:
       - `__str__()`: Returns a string representation of the menu.
       """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.JSONField()  # JSONField for structured data

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.date}"


class Employee(models.Model):
    """
       Represents an employee.

       Fields:
       - `name` (CharField): The name of the employee (maximum length: 255 characters).
       - `email` (EmailField): The email address of the employee (must be unique).

       Methods:
       - `__str__()`: Returns the name of the employee as a string.
       """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    """
       Represents a vote mechanism by an employee for a specific menu.

       Fields:
       - `employee` (ForeignKey to Employee): The employee who voting.
       - `menu` (ForeignKey to Menu): The menu for which the vote is cast.

       Methods:
       - `__str__()`: Returns a string representation of the vote.
       """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.name}'s vote for {self.menu.restaurant.name}'s menu on {self.menu.date}"