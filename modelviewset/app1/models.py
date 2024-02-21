from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    salary = models.IntegerField()
    age = models.IntegerField()


    def __str__(self):
        return self.name
    # class Meta:
    #     db_table = 'employee'