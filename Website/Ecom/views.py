from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Brand,Category,Product_Details,Cart,ShippingInfo,Carousel,promotion,ContactUs
from django.core.paginator import Paginator
from django.contrib import messages



@login_required(login_url='/login/')
def index(request, id=None):
    if id:
        companies = get_object_or_404(Brand, pk=id)
        mobiles_items = Product.objects.filter(company=companies, 
                                               category__name="Mobile Phone", trending_items=False, first_one=False)
        mobiles_first = Product.objects.filter(company=companies, 
                                               category__name="Mobile Phone", first_one=True).first()
    else:
        mobiles_items = Product.objects.filter(category__name="Mobile Phone", 
                                               trending_items=False, first_one=False)
        mobiles_first = Product.objects.filter(category__name='Mobile Phone', first_one=True).first()
    
    frist_crousel = Carousel.objects.filter(frist_crousel=True).first()
    second_crousel = Carousel.objects.filter(second_crousel=True).first()
    third_crousel = Carousel.objects.filter(third_crousel=True).first()
    
    trending = Product.objects.filter(trending_items=True, first_one=False)
    tablets_item = Product.objects.filter(category__name='Tablet', 
                                          trending_items=False, first_one=False)
    tablets_first = Product.objects.filter(category__name='Tablet', 
                                           trending_items=False, first_one=True).first()
    frist_promotion = promotion.objects.filter(first=True).first()
    second_promotion = promotion.objects.filter(second=True).first()
    third_promotion = promotion.objects.filter(three=True).first()
    four_promotion = promotion.objects.filter(four=True).first()
    five_promotion = promotion.objects.filter(five=True).first()
    all_mobile=Brand.objects.filter(category__name='Mobile Phone')    
    all_tablet=Brand.objects.filter(category__name='Tablet')
    context={
        'frist_promotion':frist_promotion,
        'second_promotion':second_promotion,
        'third_promotion':third_promotion,
        'four_promotion':four_promotion,
        'five_promotion':five_promotion,
        'all_mobile':all_mobile,
        'all_tablet':all_tablet,
        'frist_crousel':frist_crousel,
        'second_crousel':second_crousel,
        'third_crousel':third_crousel,
        'mobiles_items':mobiles_items,
        'mobiles_first':mobiles_first,
        'trending':trending,
        'tablets_item':tablets_item,
        'tablets_first':tablets_first,
        
    }      
    return render (request,'main/index.html',context)


@login_required
def index_tablet(request, id=None):
    if id:
        companies = get_object_or_404(Brand, pk=id)
        tablets_item = Product.objects.filter(company=companies, 
                                              category__name="Tablet",
                                                trending_items=False, first_one=False)
        tablets_first = Product.objects.filter(company=companies, 
                                               category__name="Tablet", first_one=True).first()
    else:
        tablets_item = Product.objects.filter(category__name="Tablet", 
        trending_items=False, first_one=False)
        tablets_first = Product.objects.filter(category__name='Tablet', first_one=True).first()


    frist_crousel = Carousel.objects.filter(frist_crousel=True).first()
    second_crousel = Carousel.objects.filter(second_crousel=True).first()
    third_crousel = Carousel.objects.filter(third_crousel=True).first()

    all_mobile=Brand.objects.filter(category__name='Mobile Phone')    
    all_tablet=Brand.objects.filter(category__name='Tablet')
    trending = Product.objects.filter(trending_items=True, first_one=False)
    mobiles_items = Product.objects.filter(category__name='Mobile Phone',
                                            trending_items=False, first_one=False)
    mobiles_first = Product.objects.filter(category__name='Mobile Phone',
                                            trending_items=False, first_one=True).first()
    context={
        'frist_crousel':frist_crousel,
        'second_crousel':second_crousel,
        'third_crousel':third_crousel,
        'all_tablet':all_tablet,
        'all_mobile':all_mobile,
        'mobiles_items':mobiles_items,
        'mobiles_first':mobiles_first,
        'trending':trending,
        'tablets_item':tablets_item,
        'tablets_first':tablets_first,
    } 
    return render (request,'main/index.html',context)



@login_required
def about_us(request):
    return render(request, 'main/about_us.html')

@login_required
def search_results(request):
    
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query:
            results = Product.objects.filter(name__icontains=search_query)
        else:
            results = Product.objects.all() 
        return render(request, 'main/search_results.html', {'results': results})
    return render(request, 'main/search_results.html', {'results': []})
 


@login_required
def product_details(request ,id=None):
    item = None  
    if id:
        item = get_object_or_404(Product, id=id)
    else:

        item=Product.objects.all().first()
    details = Product_Details.objects.all().first()
    trending = Product.objects.filter(trending_items=True, first_one=False)
    reviews = Reviews.objects.filter(product=item)
    context={
        'trending':trending,
        'details':details,
        'item':item,
        'reviews':reviews
    }
    return render(request, 'main/product_detail.html',context)


from .models import Reviews

def submit_review(request, id):
    url = request.META.get('HTTP_REFERER')  
    if request.method == "POST":
        try:
            review = Reviews.objects.get(user=request.user, product_id=id)
            review.subject = request.POST.get('subject')
            review.review = request.POST.get('review')
            review.rating = request.POST.get('rating')
            review.save()
            messages.success(request, "Your review has been updated")
            return redirect(url)
        except Reviews.DoesNotExist:
            review = Reviews(
                subject=request.POST.get('subject'),
                review=request.POST.get('review'),
                rating=request.POST.get('rating'),
                product_id=id,
                user=request.user
            )
            review.save()
            messages.success(request, "Your review has been submitted")
            return redirect(url)
    else:
        messages.error(request, "Invalid request")
        return redirect(url) 
    

    
@login_required
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            messages.error(request, "Please enter valid data.")
            return redirect('contact_us')

        
        contact_us = ContactUs(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact_us.save()
        messages.success(request, "Thank you for your message.")
        return redirect('contact_us')

    return render(request, 'main/contact_us.html')



@login_required
def product(request, id=None):
    if id:
        category = get_object_or_404(Category, id=id)
        item_list = Product.objects.filter(category=category)
    else:
        item_list = Product.objects.all()
    
    paginator = Paginator(item_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'category':category,
    }
    return render(request, 'main/product.html', context)




@login_required
def checkout_info(request):
    user = request.user

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        area_code = request.POST.get('area_code')
        primary_phone = request.POST.get('primary_phone')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        zip_code = request.POST.get('zip_code')
        business_address = request.POST.get('business_address') == '1'  

        if first_name and last_name and area_code and primary_phone and address_1 and zip_code:
            try:
                ch = ShippingInfo(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    company_name=company_name,
                    area_code=area_code,
                    primary_phone=primary_phone,
                    address_1=address_1,
                    address_2=address_2,
                    zip_code=zip_code,
                    business_address=business_address
                )
                ch.save()
                messages.success(request, "Checkout information submitted successfully.")
                
                return redirect('checkout_payment') 
            except Exception :
                messages.error(request, "An error occurred in Checkout information")
                
                return redirect('checkout_info') 
    else:
        print('Not a POST request.')
    return render(request, 'main/checkout_info.html')




@login_required
def my_account(request):
    return render(request, 'main/my_account.html')



@login_required
def index_inverse_header(request):
    return render(request, 'main/index_inverse_header.html')


@login_required
def index_fixed_header(request):
    return render(request, 'main/index_fixed_header.html')


@login_required
def faq(request):
    return render(request, 'main/faq.html')




@login_required
def checkout_cart(request, id=None):
    if id:
        product = Product.objects.get(id=id)
        user = request.user
        Cart.objects.get_or_create(
            user=user,
            product=product,
            defaults={'price': product.price, 'quantity': 1}
        )

    user = request.user   
    carts = Cart.objects.filter(user=user)
    amount = 0
    shipping = 0
    total_amount=0
    if carts :
        for cart_item in carts:
            cart_item.total_price = cart_item.price * cart_item.quantity
            total_price =cart_item.price * cart_item.quantity 
            shipping += cart_item.quantity * 10 
            amount += total_price
            total_amount +=shipping +total_price
        
    context={
        'carts':carts,
        'amount':amount,
        'shipping':shipping,
        'cart_subtotal':total_amount
    }    
    return render(request, 'main/checkout_cart.html',context)


def delete_cart_item(request, id):
    user = request.user
    cart_item = get_object_or_404(Cart, id=id, user=user)
    cart_item.delete()
    return redirect('checkout')



def increase_quantity(request, id):
    user = request.user
    cart_item = get_object_or_404(Cart, id=id, user=user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('checkout')  


def decrease_quantity(request, id):
    user = request.user
    cart_item = get_object_or_404(Cart, id=id, user=user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('checkout')



@login_required
def checkout_payment(request):
    user = request.user   
    carts = Cart.objects.filter(user=user)
    amount = 0
    shipping = 0
    if carts:
        for cart_item in carts:
            total_price = cart_item.price * cart_item.quantity
            shipping += cart_item.quantity * 10
            amount += total_price
    total_amount = shipping + amount
    context={
        'total_amount':total_amount
    }

    return render(request, 'main/checkout_payment.html',context )



from payments.models import Payment

@login_required
def checkout_complete(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    if carts:
        for i in carts:
            i.shipping= i.quantity * 10        
    payment_info = Payment.objects.filter(user=user)
    
    if payment_info:
        cart = Cart.objects.filter(user=user)
        cart.delete()
        
    context={
        'payment_info':payment_info,
        'carts':carts,
    }
    return render(request, 'main/checkout_complete.html',
                   context)





