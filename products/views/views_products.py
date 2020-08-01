from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from laboratory.models import Department
from products.forms import *
from django.db.models import F
from datetime import datetime, timedelta
from django.views.generic.list import ListView
from el_pagination.decorators import page_templates
from basket.forms import BasketAddProductForm

class ProductSearchListView(ListView):
    """
    Display a Product List page filtered by the search query.
    """

    model = Product
    template_name = 'search_list.html'

 #   paginate_by = 10

    def get_queryset(self):
        result = super(ProductSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            result = result.filter(name__name__icontains=query)
        else:
            result = "NOTHING FOUND"

        return result

@login_required
def stocks(request):
	all_products = Product.objects.all().exclude(remaining__lt = 1)
	stocks_total = all_products.count()
    # cart_product_form = BasketAddProductForm()
	page = request.GET.get('page', 1)
	paginator = Paginator(all_products, 10)

	try:
	    products = paginator.page(page)
	except PageNotAnInteger:
	    products = paginator.page(1)
	except EmptyPage:
	    products = paginator.page(paginator.num_pages)

	return render(request, 'products/stocks.html',
			{'allProducts': products,
			'stocks_total': stocks_total,
            'department_id': 1}
		)

@login_required
def stock_new(request, department_id):
    department = Department.objects.get(pk=department_id)
    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['remaining'] = request.POST['quantity_received']
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products:stock_detail', department_id= department_id, pk=product.pk )
    else:
        initial = {
            'received_by': request.user,
            'department': department
        }
        form = ProductForm(initial = initial)

    return render(request, 'products/stock_edit.html', {'form': form})

@login_required
def stock_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products:stock_detail',department_id=product.department.pk, pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/stock_edit.html', {'form': form})

@login_required
def stock_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products:stocks')

@login_required
def departmental_stocks(request, department_id):
	department = get_object_or_404(Department, pk=department_id)
	all_department_stocks = department.product_from.all()
	department_stock_count = all_department_stocks.count()
	return render(request, 'products/departmental_stocks.html',
			{'department': department,
            'department_id': department_id,
			'allProducts': all_department_stocks,
			'stocks_total': department_stock_count}
		)

@login_required
@page_templates({
    'products/paginate_transactions_stock_detail.html': None,
    'products/paginate_adjustments_stock_detail.html': 'adjustments_page',
})

def stock_detail(request, department_id, pk, template='products/stock_detail.html', extra_context=None):
    product = get_object_or_404(Product, pk=pk)
    stock_transactions = product.product_transaction.all()
    stock_adjustments = product.product_adjustment.all()
    basket_product_form = BasketAddProductForm()
    context = {
        'product': product,
        'basket_product_form': basket_product_form,
        'transactions': stock_transactions,
        'adjustments': stock_adjustments,
        'department_id': department_id
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request,template, context)

@login_required
def out_of_stock(request):
    # Products that are out of stock
    out_of_stock = Product.objects.filter(remaining__exact='0')
    out_of_stock_count = out_of_stock.count()
    return render(request, 'products/out_of_stock.html',
            {'allProducts': out_of_stock,
            'stocks_total': out_of_stock_count,
            'department_id': 1,
            }
        )

@login_required
def at_minimum_stock(request):
    start_date = datetime.now()
    at_min_stock = Product.objects.filter(remaining__exact=F('minimum_level')).exclude(expiry_date__lt=start_date)
    at_min_stock_count = at_min_stock.count()
    return render(request, 'products/at_minimum_stock.html',
            {'allProducts': at_min_stock,
            'stocks_total': at_min_stock_count,
            'department_id': 1,
            }
        )

@login_required
def below_minimum_stock(request):
    start_date = datetime.now()
    below_min_stock = Product.objects.filter(remaining__gte='1', remaining__lt=F('minimum_level')).exclude(expiry_date__lt=start_date)
    below_min_stock_count = below_min_stock.count()
    return render(request, 'products/below_minimum_stock.html',
            {'allProducts': below_min_stock,
            'stocks_total': below_min_stock_count,
            'department_id': 1,
            }
        )
def over_maximum_stock(request):
    start_date = datetime.now()
    over_stock = Product.objects.filter(remaining__gt=F('minimum_level') * 2).exclude(expiry_date__lt=start_date)
    over_stock_count = over_stock.count()
    return render(request, 'products/over_maximum_stock.html',
            {'allProducts': over_stock,
            'stocks_total': over_stock_count,
            'department_id': 1,
            }
        )

@login_required
def approaching_minimum_stock(request):
    start_date = datetime.now()
    appr_min_stock = Product.objects.filter(remaining__gte=F('minimum_level') + 1, remaining__lte=F('minimum_level') + 2).exclude(expiry_date__lt=start_date)
    appr_min_stock_count = appr_min_stock.count()
    return render(request, 'products/approaching_minimum_stock.html',
            {'allProducts': appr_min_stock,
            'stocks_total': appr_min_stock_count,
            'department_id': 1,
            }
        )

@login_required
def expired_stock(request):
    start_date = datetime.now()
    expired = Product.objects.filter(expiry_date__lt=start_date).exclude(remaining__exact='0').exclude(remaining__exact='0')
    expired_count = expired.count()
    return render(request, 'products/expired_stock.html',
            {'allProducts': expired,
            'stocks_total': expired_count,
            'department_id': 1,
            }
        )
@login_required
def expire_this_week_stock(request):
    start_date = datetime.now()
    end_date = datetime.now() + timedelta(days=7)
    expire_this_week = Product.objects.filter(expiry_date__range=(start_date, end_date)).exclude(remaining__exact='0')
    expire_this_week_count = expire_this_week.count()
    return render(request, 'products/expire_this_week_stock.html',
            {'allProducts': expire_this_week,
            'stocks_total': expire_this_week_count,
            'department_id': 1,
            }
        )

@login_required
def expire_this_month_stock(request):
    start_date = datetime.now()
    month_end_date = datetime.now() + timedelta(days=30)
    expire_this_month = Product.objects.filter(expiry_date__range=(start_date, month_end_date)).exclude(remaining__exact='0')
    expire_this_month_count = expire_this_month.count()
    return render(request, 'products/expire_this_month_stock.html',
            {'allProducts': expire_this_month,
            'stocks_total': expire_this_month_count,
            'department_id': 1,
            }
        )

@login_required
def expire_today_stock(request):
    expire_today = Product.objects.filter(expiry_date__exact=datetime.now()).exclude(remaining__exact='0')
    expire_today_count = expire_today.count()
    return render(request, 'products/expire_today_stock.html',
            {'allProducts': expire_today,
            'stocks_total': expire_today_count,
            'department_id': 1,
            }
        )
