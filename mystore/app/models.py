from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
STATE_CHOICES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    mob=models.CharField(max_length=12,default= +91)
    # locality=models.CharField(max_length=150)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=55)

    def __str__(self):
        return str(self.id)

MY_CATEGORY_CHOICE=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BM','Bottom Wear'),
)

class Product(models.Model):
    title=models.CharField(max_length=55)
    selling_price=models.FloatField(max_length=55)
    discounted_price=models.FloatField(max_length=55)
    description=models.TextField()
    brand=models.CharField(max_length=155)
    category=models.CharField(choices=MY_CATEGORY_CHOICE,max_length=3)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_amt(self):
        return self.quantity * self.product.discounted_price

STATUS_OF_PRODUCT=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Deleverd','Deleverd'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=59,choices=STATUS_OF_PRODUCT,default='Pending')

    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price