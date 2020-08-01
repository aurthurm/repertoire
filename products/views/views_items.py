from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from products.forms import *
from django.views.generic.list import ListView

class ItemSearchListView(ListView):
    """
    Display a Product List page filtered by the search query.
    """

    model = Item
    template_name = 'search_list.html'

 #   paginate_by = 10

    def get_queryset(self):
        result = super(ItemSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            result = result.filter(name__icontains=query)
        else:
            result = "NOTHING FOUND"

        return result


@login_required
def items(request):
	all_items = Item.objects.all()
	items_count = all_items.count()
	page = request.GET.get('page', 1)
	paginator = Paginator(all_items, 50)

	try:
	    items = paginator.page(page)
	except PageNotAnInteger:
	    items = paginator.page(1)
	except EmptyPage:
	    items = paginator.page(paginator.num_pages)

	return render(request, 'products/items.html',
			{'items': items,
			'items_count': items_count}
		)

@login_required
def item_detail(request, pk):
	item = get_object_or_404(Item, pk=pk)
	return render(request, 'products/item_detail.html',
			{'item': item}
		)

@login_required
def departmental_items(request, pk):
	department = get_object_or_404(Department, pk=pk)
	all_departments_items = department.item_from.all()
	all_departments_items_count = all_departments_items.count()
	return render(request, 'products/departmental_items.html',
			{'department': department,
			'items': all_departments_items,
			 'items_count': all_departments_items_count}
		)


@login_required
def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
   #     return redirect('lab_inventory:item_detail', pk=item.pk)
        return redirect('products:items')
    else:
        form = ItemForm()

    return render(request, 'products/item_edit.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('products:item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'products/item_edit.html', {'form': form})

@login_required
def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('products:items')
