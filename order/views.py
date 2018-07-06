from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import OrderProduct
from .forms import *
from basket.basket import Basket
from datetime import datetime
from django.db.models import F
from .models import Order
from movements.models import Transaction


def get_order_number():
    list_date = list(str(datetime.now()))
    slices = list_date[:4] + list_date[5:7] + list_date[8:10] + list_date[11:13] + list_date[14:16] + list_date[17:19] + list_date[20:]
    order_num = ""
    for slice in slices:
        order_num += slice
    return order_num

def order_create(request):
    basket = Basket(request)
    user = request.user
    if request.method == "POST":
        order_numbr = get_order_number()
        request.POST = request.POST.copy()
        request.POST['order_number'] = order_numbr
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in basket:
                OrderProduct.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
                )
            #clear basket
            basket.clear()
            return render(request, 'order/created.html', {'order_number': order.order_number})
    else:
        form = OrderCreateForm(initial={'order_by': user})
    return render(request, 'order/create.html', {
        'basket': basket,
        'form': form
    })

def orders(request):
    all_unprocessed_orders = Order.objects.all().filter(order_state__exact=False)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_unprocessed_orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'order/orders.html', {'allOrders':orders})

def processed_orders(request):
    all_processed_orders = Order.objects.all().filter(order_state__exact=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_processed_orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'order/processed-orders.html', {'allOrders':orders})

def view_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    all_products = order.prdcts.all()
    # products_dict = {}
    # for product in all_products:
    #     products_dict[product] = {'remaining': product.product.remaining, 'quantity': product.quantity, 'price': product.price}
    #
    # for item in products_dict:
    #     item['update_quantity_form'] = OrderUpdateForm(initial={'quantity': item.quantity, 'update': True})
    return render(request, 'order/order-detail.html', {'order':order, 'all_products':all_products})

def process_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    all_products = order.prdcts.all()
    for product in all_products:
        Transaction.objects.create(
            product=product.product,
            issued=product.quantity,
            issued_to=order.ordering_dept,
            transaction_by=request.user
        )
    order.order_state = True
    order.save()
    return render(request, 'order/processed.html')
