from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    search_fields=['name',]
   
class BrandAdmin(admin.ModelAdmin):
    list_display = ('category','brand','id')
    search_fields = ['category','brand']




class ProductAdmin(admin.ModelAdmin):
    list_display=('category','company','name','off','price','id')
    search_fields=['name','company',]


class PromotionsAdmin(admin.ModelAdmin):
    list_display=('name','id')
    search_fields=['name',]


class CartAdmin(admin.ModelAdmin):
    list_display=('user','product','price','quantity','id')
    search_fields=['user','quantity',]




class ShippingInfoAdmin(admin.ModelAdmin):
    list_display=('user','first_name','company_name','zip_code','id')
    search_fields=['user','first_name','zip_code']


class CarouselAdmin(admin.ModelAdmin):
    list_display=('name','id')


class User_Card_infoAdmin(admin.ModelAdmin):
    list_display=('cardholder','card_number','expiration_date','csc')


admin.site.register(User_Card_info,User_Card_infoAdmin)   
admin.site.register(Reviews)
admin.site.register(ContactUs)
admin.site.register(promotion,PromotionsAdmin)
admin.site.register(Carousel,CarouselAdmin)
admin.site.register(ShippingInfo,ShippingInfoAdmin)    
admin.site.register(Cart,CartAdmin)    
admin.site.register(Category,CategoryAdmin) 
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Product_Details)