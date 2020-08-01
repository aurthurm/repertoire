from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from products.forms import *


@login_required
def hazards(request):
    hazards = Hazard.objects.all()
    hazards_count = hazards.count()
    return render(request, 'products/hazards.html',
                  {'multies': hazards,
                   'multies_count': hazards_count})

@login_required
def hazard_detail(request, pk):
    hazard = get_object_or_404(Hazard, pk=pk)
    return render(request, 'products/hazard_detail.html',
            {'multi': hazard}
        )


@login_required
def hazard_new(request):
    if request.method == "POST":
        form = HazardForm(request.POST)
        if form.is_valid():
            hazard = form.save(commit=False)
            hazard.save()
 #       return redirect('lab_inventory:hazard_detail', pk=hazard.pk)
        return redirect('products:hazards')
    else:
        form = HazardForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def hazard_edit(request, pk):
    hazard = get_object_or_404(Hazard, pk=pk)
    if request.method == "POST":
        form = HazardForm(request.POST, instance=hazard)
        if form.is_valid():
            hazard = form.save(commit=False)
            hazard.save()
            return redirect('products:hazard_detail', pk=hazard.pk)
    else:
        form = HazardForm(instance=hazard)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def hazard_remove(request, pk):
    hazard = get_object_or_404(Hazard, pk=pk)
    hazard.delete()
    return redirect('products:hazards')
