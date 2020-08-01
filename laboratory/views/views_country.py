from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from laboratory.models import *
from laboratory.forms import *

@login_required
def countries(request):
    countries = Country.objects.all()
    countries_count = countries.count()
    return render(request, 'laboratory/countries.html',
                  {'multies': countries,
                   'multies_count': countries_count})

@login_required
def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'laboratory/country_detail.html',
            {'multi': country}
        )

@login_required
def country_new(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
#        return redirect('laboratory:country_detail', pk=country.pk)
        return redirect('laboratory:countries')
    else:
        form = CountryForm()

    return render(request, 'multi_edit.html', {'form': form})

@login_required
def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            county = form.save(commit=False)
            country.save()
            return redirect('laboratory:country_detail', pk=country.pk)
    else:
        form = CountryForm(instance=country)
    return render(request, 'multi_edit.html', {'form': form})

@login_required
def country_remove(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.delete()
    return redirect('laboratory:countries')
