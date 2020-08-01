from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from products.forms import *


@login_required
def categories(request):
	categories = Category.objects.all()
	categories_count = categories.count()
	return render(request, 'products/categories.html',
				  {'multies': categories,
				   'multies_count': categories_count})

@login_required
def category_detail(request, pk):
	category = get_object_or_404(Category, pk=pk)
	return render(request, 'products/category_detail.html',
			{'multi': category}
		)


@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
 #       return redirect('lab_inventory:category_detail', pk=category.pk)
        return redirect('products:categories')
    else:
        form = CategoryForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('products:category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def category_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('products:categories')
