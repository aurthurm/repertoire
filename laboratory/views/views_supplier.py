from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from laboratory.models import *
from laboratory.forms import *

@login_required
def suppliers(request):
	all_suppliers = Supplier.objects.all()
	return render(request, 'laboratory/suppliers.html',
			{'suppliers': all_suppliers}
		)

@login_required
def supplier_detail(request, pk):
	supplier = get_object_or_404(Supplier, pk=pk)
	return render(request, 'laboratory/supplier_detail.html',
			{'supplier': supplier}
		)

@login_required
def supplier_new(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
        return redirect('laboratory:supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm()

    return render(request, 'laboratory/supplier_edit.html', {'form': form})

@login_required
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
            return redirect('laboratory:supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'laboratory/supplier_edit.html', {'form': form})

@login_required
def supplier_remove(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('laboratory:suppliers')
