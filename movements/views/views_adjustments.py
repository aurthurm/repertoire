from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django_tables2 import RequestConfig
from movements.forms import *
from movements.tables import *
from products.models import Product

@login_required
def adjustment_new(request, pk):
    user = request.user
    stock = Product.objects.get(pk=pk)
    available_stock = stock.remaining
    product_name = stock.name
    if request.method == "POST":
        form = AdjustmentForm(request.POST)
        if form.is_valid():
            adjustment = form.save(commit=False)
            adjustment.save()
        return redirect('products:stock_detail', department_id=stock.department.pk, pk=pk)
    else:
        initial = {
            'product': stock,
            'adjustment_by': user
        }
        form = AdjustmentForm(initial = initial)
        # form.fields['product'].initial = stock
        # form.fields['user'].initial = user

    return render(request, 'movements/adjustment_edit.html', {
    'form': form,
    'available_stock': available_stock,
    'check': 'AdjustmentNew'
    })

@login_required
def new_adjustment(request):
    if request.method == "POST":
        form = AdjustmentForm(request.POST)
        if form.is_valid():
            adjustment = form.save(commit=False)
            adjustment.save()
        return redirect('movements:adjustments')
    else:
        form = AdjustmentForm()

    return render(request, 'movements/adjustment_edit.html', {'form': form})

@login_required
def adjustments(request):
    all_adjustments = AdjustmentTable(Adjustment.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(all_adjustments)

    return render(request, 'movements/adjustments.html',{'adjustments': all_adjustments})
