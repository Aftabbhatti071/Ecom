$(document).ready(function(){
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    function updateCartTotal() {
        let subtotal = 0;
        let shipping = 0;
        $('.total-price').each(function() {
            let quantity = $(this).closest('tr').find('input[name="qty"]').val();
            subtotal += parseFloat($(this).text());
            shipping += 10 * parseInt(quantity); // Assuming $10 shipping per item
        });
        let total = subtotal + shipping;
        $('#cart-subtotal').text(subtotal.toFixed(2));
        $('#cart-shipping').text(shipping.toFixed(2));
        $('#cart-total').text(total.toFixed(2));
    }

    $('.qty-control').click(function(event){
        event.preventDefault();
        var button = $(this);
        var input = $(button.data('target'));
        var currentQty = parseInt(input.val());
        var productId = button.closest('td').data('product-id');

        var newQty;
        if (button.data('click') === 'increase-qty') {
            newQty = currentQty + 1;
        } else if (button.data('click') === 'decrease-qty') {
            if (currentQty > 1) {
                newQty = currentQty - 1;
            } else {
                return; // Prevent decreasing below 1
            }
        } else {
            return;
        }

        $.ajax({
            url: '/update_cart_quantity/',
            method: 'POST',
            data: {
                'product_id': productId,
                'quantity': newQty,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response){
                if(response.status === 'success') {
                    input.val(newQty);
                    var row = button.closest('tr');
                    var price = parseFloat(row.find('.cart-price').text().replace('$', ''));
                    row.find('.total-price').text((price * newQty).toFixed(2));

                    updateCartTotal();
                }
            },
            error: function(response){
                console.log("Error updating quantity");
            }
        });
    });

    $('.delete-cart-item').click(function(event){
        event.preventDefault();
        var button = $(this);
        var productId = button.data('product-id');

        $.ajax({
            url: '/delete_cart_item/',
            method: 'POST',
            data: {
                'product_id': productId,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response){
                if(response.status === 'success') {
                    button.closest('tr').remove();
                    updateCartTotal();
                }
            },
            error: function(response){
                console.log("Error deleting cart item");
            }
        });
    });

    updateCartTotal(); // Initial calculation
});
