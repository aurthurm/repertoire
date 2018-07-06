from ajax_select import register, LookupChannel
from .models import Item, Product

@register('items')
class ItemLookup(LookupChannel):

	model = Item

	def get_query(self, q, request):
		return self.model.objects.filter(name__icontains=q).order_by('name')

	def format_item_display(self, item):
		return u"<span class='item'>%s</span>" % item.name