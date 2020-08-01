from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig
from movements.forms import *
from movements.tables import *
from products.models import Product


@login_required
def transaction_new(request, pk):
    user = request.user
    stock = Product.objects.get(pk=pk)
    available_stock = stock.remaining
    product_name = stock.name
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
        return redirect('products:stock_detail',department_id=stock.department.pk,  pk=pk)
    else:
        initial = {
            'product': stock,
            'transaction_by': user
        }
        form = TransactionForm(initial = initial)

    return render(request, 'movements/transaction_edit.html', {
        'form': form,
        'available_stock': available_stock,
        'product_name': product_name,
        'check': 'TransactionNew'
    })

@login_required
def new_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
        return redirect('movements:transactions')
    else:
        form = TransactionForm()

    return render(request, 'movements/transaction_edit.html', {'form': form})

@login_required
def transactions(request):
    all_transactions = TransactionTable(Transaction.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(all_transactions)

    return render(request, 'movements/transactions.html',{'transactions': all_transactions})
