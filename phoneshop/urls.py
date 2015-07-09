from django.conf.urls import url
from views import create, get_product_detail, get_all_products, update_product, \
    delete_product, create_test

urlpatterns = [
    url(r'^create/$', create),
    url(r'^get_product_detail/$', get_product_detail),
    url(r'^get_all_products/$', get_all_products),
    url(r'^update_product/$', update_product),
    url(r'^delete_product/$', delete_product),

    url(r'^create_test/$', create_test),
]