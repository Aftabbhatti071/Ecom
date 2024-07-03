from .models import Category, Product, Brand ,Cart

def category_processor(request):
    categories = Category.objects.all()
    ipad_items = Product.objects.filter(category__name="Mobile Phone",company__brand='ipad')
    Sumsung_items = Product.objects.filter(category__name="Mobile Phone",company__brand='Sumsung')
    Sony_items = Product.objects.filter(category__name="Mobile Phone",company__brand='Sony')
    Microsoft_items = Product.objects.filter(category__name="Mobile Phone",company__brand='Microsoft')
    user = request.user
    carts = []
    item_cart = 0

    if user.is_authenticated:
        carts = Cart.objects.filter(user=user)
        for cart_item in carts:
            item_cart += 1
            cart_item.total_price = cart_item.price * cart_item.quantity

    return {
        'item_cart':item_cart,
        'carts':carts,
        'categories': categories,
        'ipad_items':ipad_items,
        'Sumsung_items':Sumsung_items,
        'Microsoft_items':Microsoft_items,
        'Sony_items':Sony_items,
        'carts':carts,
    }
