from django.db import models
from Customer.models import Customer

# Create your models here.



class CustomerProfile(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures',
                                        default= 'default.jpg')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    about = models.TextField(blank=True)


    



