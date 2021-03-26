from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    pizza_type = models.CharField(max_length=100)
    pizza_size = models.CharField(max_length=100)
    topping_type =  models.CharField(max_length=100)

    def __str__(self):
        return self.pizza_type

        

    
    

     
 