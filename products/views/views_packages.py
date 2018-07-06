from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from products.models import *
from products.forms import *


@login_required
def packages(request):
	packages = PackageType.objects.all()
	packages_count = packages.count()
	return render(request, 'products/packages.html',
				  {'multies': packages,
				   'multies_count': packages_count})

@login_required
def package_detail(request, pk):
	package = get_object_or_404(PackageType, pk=pk)
	return render(request, 'products/package_detail.html',
			{'multi': package}
		)


@login_required
def package_new(request):
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.save()
#        return redirect('lab_inventory:package_detail', pk=package.pk)
        return redirect('products:packages')
    else:
        form = PackageForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def package_edit(request, pk):
    package = get_object_or_404(PackageType, pk=pk)
    if request.method == "POST":
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            package = form.save(commit=False)
            package.save()
            return redirect('products:package_detail', pk=package.pk)
    else:
        form = PackageForm(instance=package)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def package_remove(request, pk):
    package = get_object_or_404(PackageType, pk=pk)
    package.delete()
    return redirect('products:packages')
