from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from laboratory.models import *
from laboratory.forms import *


@login_required
def laboratories(request):
    laboratories = Laboratory.objects.all()
    laboratories_count = laboratories.count()
    return render(request, 'laboratory/laboratories.html',
                  {'multies': laboratories,
                   'multies_count': laboratories_count})

@login_required
def laboratory_detail(request, pk):
    laboratory = get_object_or_404(Laboratory, pk=pk)
    return render(request, 'laboratory/laboratory_detail.html',
            {'multi': laboratory}
        )

@login_required
def laboratory_new(request):
    if request.method == "POST":
        form = LaboratoryForm(request.POST)
        if form.is_valid():
            laboratory = form.save(commit=False)
            laboratory.save()
 #       return redirect('laboratory:laboratory_detail', pk=laboratory.pk)
        return redirect('laboratory:laboratories')
    else:
        form = LaboratoryForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def laboratory_edit(request, pk):
    laboratory = get_object_or_404(Laboratory, pk=pk)
    if request.method == "POST":
        form = LaboratoryForm(request.POST, instance=laboratory)
        if form.is_valid():
            laboratory = form.save(commit=False)
            laboratory.save()
            return redirect('laboratory:laboratory_detail', pk=laboratory.pk)
    else:
        form = LaboratoryForm(instance=laboratory)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def laboratory_remove(request, pk):
    laboratory = get_object_or_404(Laboratory, pk=pk)
    laboratory.delete()
    return redirect('laboratory:laboratories')
