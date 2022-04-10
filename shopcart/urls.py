from django.urls import path
from . import views

urlpatterns = [
    path('cartdetails',views.cartlist,name='cartdetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('decrement/<int:product_id>/',views.del_cart,name='decrement'),
    path('remove/<int:product_id>/',views.removeall_cart,name='remove')
]