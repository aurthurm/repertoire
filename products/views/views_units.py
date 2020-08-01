from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from products.forms import *


@login_required
def units(request):
	units = Unit.objects.all()
	units_count = units.count()
	return render(request, 'products/units.html',
				  {'multies': units,
				   'multies_count': units_count})

@login_required
def unit_detail(request, pk):
	unit = get_object_or_404(Unit, pk=pk)
	return render(request, 'products/unit_detail.html',
			{'multi': unit}
		)


@login_required
def unit_new(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()
 #       return redirect('lab_inventory:unit_detail', pk=unit.pk)
        return redirect('products:units')
    else:
        form = UnitForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def unit_edit(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == "POST":
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()
            return redirect('products:unit_detail', pk=unit.pk)
    else:
        form = UnitForm(instance=unit)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def unit_remove(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    unit.delete()
    return redirect('products:units')
