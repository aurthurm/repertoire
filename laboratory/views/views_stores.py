from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from laboratory.models import *
from laboratory.forms import *

@login_required
def stores(request):
	stores = Store.objects.all()
	stores_count = stores.count()
	return render(request, 'laboratory/stores.html',
				  {'multies': stores,
				   'multies_count': stores_count})

@login_required
def store_detail(request, pk):
	store = get_object_or_404(Store, pk=pk)
	return render(request, 'laboratory/store_detail.html',
			{'multi': store}
		)

@login_required
def store_new(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()
 #       return redirect('lab_inventory:store_detail', pk=store.pk)
        return redirect('laboratory:stores')
    else:
        form = StoreForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def store_edit(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()
            return redirect('laboratory:store_detail', pk=store.pk)
    else:
        form = StoreForm(instance=store)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def store_remove(request, pk):
    store = get_object_or_404(Store, pk=pk)
    store.delete()
    return redirect('laboratory:stores')
