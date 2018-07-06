from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from laboratory.models import *
from laboratory.forms import *

@login_required
def departments(request):
	all_departments = Department.objects.all()
	return render(request, 'laboratory/departments.html',
			{'all_departments': all_departments}
		)


@login_required
def departments_list(request):
    departments = Department.objects.all()
    departments_count = departments.count()
    return render(request, 'laboratory/departments_list.html',
                  {'multies': departments,
                   'multies_count': departments_count})

@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'laboratory/department_detail.html',
            {'multi': department}
        )

@login_required
def department_new(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
 #       return redirect('lab_inventory:department_detail', pk=department.pk)
        return redirect('laboratory:departments_list')
    else:
        form = DepartmentForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('laboratory:department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def department_remove(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('laboratory:departments')
