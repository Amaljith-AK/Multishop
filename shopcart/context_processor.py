from .models import *
from .views import *


def counts(request):
    item_count=0;
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = CartList.objects.filter(card_id=cart_no(request))
            cti = Items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count += c.quantity
        except CartList.DoesNotExist:
            item_count = 0
        return dict(itc = item_count)
