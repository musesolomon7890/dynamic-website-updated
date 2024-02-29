from django.db import models



class product(models.Model):
    product_name = models.TextField()
    product_dis = models.TextField()
    image = models.ImageField(null=True)
    price =  models.TextField(null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

def __str__(self) -> str:
   return self.product_name

class home(models.Model):
    image = models.ImageField(null=True)
    
class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    

def __str__(self):
        return self.name