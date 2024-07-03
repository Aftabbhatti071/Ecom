from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255,unique=True , default=None)

    def __str__(self):
        return self.name


class Brand(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
    brand=models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'{self.brand}  of {self.category}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='media/')
    off=models.IntegerField()
    price=models.FloatField()
    discount=models.FloatField()  
    short_desc = models.CharField(max_length=100)      
    trending_items=models.BooleanField(default=False)
    first_one=models.BooleanField(default=False)




class Product_Details(models.Model):
    warranty = models.IntegerField()
    display = models.CharField(max_length=100)
    fingerprint = models.CharField(max_length=100, default=None)
    chip = models.CharField(max_length=100, default=None)
    camera = models.CharField(max_length=100, default=None)
    camera_recording = models.CharField(max_length=100, default=None)
    operating_system = models.CharField(max_length=100, default=None)
    
   
    
    STOCK_CHOICES = [
        ('In stock', 'In stock'),
        ('Out stock', 'Out stock'),
    ]
    
    availability = models.CharField(max_length=70, choices=STOCK_CHOICES)
    look_desc = models.TextField()
    look_img = models.ImageField(upload_to='pics')
    touch_desc = models.TextField()
    touch_img = models.ImageField(upload_to='pics')
    cameras_desc = models.TextField()
    cameras_img = models.ImageField(upload_to='pics')
    technology_desc = models.TextField()
    technology_img = models.ImageField(upload_to='pics')
    design_desc = models.TextField()
    design_img = models.ImageField(upload_to='pics')

    def __str__(self):
        return f'Details for {self.availability}'
    


    

class Carousel(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    back_img = models.ImageField(upload_to='pics')
    frist_crousel=models.BooleanField(default=False)
    second_crousel=models.BooleanField(default=False)
    third_crousel=models.BooleanField(default=False)

    def __str__(self):
        return self.name.name
    

class promotion(models.Model):
    name=models.ForeignKey(Product,on_delete=models.CASCADE)
    first=models.BooleanField(default=False)
    second=models.BooleanField(default=False) 
    three=models.BooleanField(default=False) 
    four=models.BooleanField(default=False) 
    five=models.BooleanField(default=False)     
    


from django.contrib.auth.models import User
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"
    

class ShippingInfo(models.Model):
    user=models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.CharField(max_length=10)
    primary_phone = models.CharField(max_length=15)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    business_address = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.address_1}"



class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject
    



class Reviews(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField( max_length=100, blank=True)
    review=models.TextField(blank=True, max_length=500)
    rating=models.FloatField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user    
    
    



class User_Card_info(models.Model):
    user=models.CharField(max_length=255)
    cardholder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)  
    expiration_date = models.DateField()
    csc = models.CharField(max_length=4) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.cardholder.username}'s Card"
