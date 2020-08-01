from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from datetime import datetime, timedelta
from products.models import Product

@login_required
def dashboard(request):
    start_date = datetime.now()
    # Products that are out of stock
    out_of_stock = Product.objects.filter(remaining__exact='0')
    out_of_stock_count = out_of_stock.count()
    # Products that above maximum stock but not counting the expired
    over_stock = Product.objects.filter(remaining__gt=F('minimum_level') * 2).exclude(expiry_date__lt=start_date)
    over_stock_count = over_stock.count()
    # Products that re below minimum stock but not out of stock
    below_min_stock = Product.objects.filter(remaining__gte='1', remaining__lt=F('minimum_level')).exclude(expiry_date__lt=start_date)
    below_min_stock_count = below_min_stock.count()
    # Products approaching minimum stock : those above minimun stock by 1 or 2 products
    appr_min_stock = Product.objects.filter(remaining__gte=F('minimum_level') + 1, remaining__lte=F('minimum_level') + 2).exclude(expiry_date__lt=start_date)
    appr_min_stock_count = appr_min_stock.count()
    #Products at minimum stock
    at_min_stock = Product.objects.filter(remaining__exact=F('minimum_level')).exclude(expiry_date__lt=start_date)
    at_min_stock_count = at_min_stock.count()
    # Expiring today
    expire_today = Product.objects.filter(expiry_date__exact=datetime.now()).exclude(remaining__exact='0')
    expire_today_count = expire_today.count()
    # Expiring in the next 7 day
    end_date = datetime.now() + timedelta(days=7)
    expire_this_week = Product.objects.filter(expiry_date__range=(start_date, end_date)).exclude(remaining__exact='0')
    expire_this_week_count = expire_this_week.count()
    # Expiring in the next 30 days
    month_end_date = datetime.now() + timedelta(days=30)
    expire_this_month = Product.objects.filter(expiry_date__range=(start_date, month_end_date)).exclude(remaining__exact='0')
    expire_this_month_count = expire_this_month.count()
    # Expired
    expired = Product.objects.filter(expiry_date__lt=start_date).exclude(remaining__exact='0').exclude(remaining__exact='0')
    expired_count = expired.count()
    return render(request, 'dashboard/index.html',
    		{'out_of_stock': out_of_stock,
    		'out_of_stock_count': out_of_stock_count,
            'over_stock': over_stock,
            'over_stock_count': over_stock_count,
    		'below_min_stock': below_min_stock,
    		'below_min_stock_count': below_min_stock_count,
    		'appr_min_stock': appr_min_stock,
    		'appr_min_stock_count': appr_min_stock_count,
    		'expire_today':expire_today,
    		'expire_today_count': expire_today_count,
    		'expire_this_week': expire_this_week,
    		'expire_this_week_count': expire_this_week_count,
            'expire_this_month': expire_this_month,
            'expire_this_month_count': expire_this_month_count,
    		'expired': expired,
    		'expired_count': expired_count,
    		'at_min_stock': at_min_stock,
    		'at_min_stock_count': at_min_stock_count
    		}
    	)

def contact_developer(request):
    contact_developer = ''
    return render(request, 'contact-developer.html', {'contact': contact_developer})

def help_section(request):
	return render(request, 'help/help.html', {'help': help_section})

def help_settings(request):
	return render(request, 'help/help-settings.html', {'help': help_settings})

def help_dashboard(request):
	return render(request, 'help/help-dashboard.html', {'help': help_dashboard})

def help_suppliers(request):
	return render(request, 'help/help-suppliers.html', {'help': help_suppliers})

def help_inventory(request):
	return render(request, 'help/help-inventory.html', {'help': help_inventory})

def help_icons(request):
	return render(request, 'help/help-icons.html', {'help': help_icons})
