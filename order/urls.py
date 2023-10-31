from django.urls import re_path

from order.views import (
    OrderViewSet, OrderItemViewSet, OrdersTodayViewSet,
    OrdersThisMonthViewSet, orders_last_month, orders_plot)

order_list = OrderViewSet.as_view({'get': 'list', 'post': 'create'})
order_detail = OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})

order_item_list = OrderItemViewSet.as_view({'get': 'list', 'post': 'create'})
order_item_detail = OrderItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})

today_orders = OrdersTodayViewSet.as_view({'get': 'list'})

this_month_orders = OrdersThisMonthViewSet.as_view({'get': 'list'})

urlpatterns = [
    re_path(r'^api/v1/order/$', order_list, name="order-list"),
    re_path(r'^api/v1/order/(?P<pk>[0-9]+)/$', order_detail, name="order-detail"),
    re_path(r'^api/v1/order/item/$', order_item_list, name="order-list"),
    re_path(r'^api/v1/order/item/(?P<pk>[0-9]+)/$', order_item_detail, name="order-item-detail"),
    re_path(r'^api/v1/order/today/$', today_orders, name='orders-today'),
    re_path(r'^api/v1/order/this-month/$', this_month_orders, name='orders-this-month'),
    re_path(r'^api/v1/order/last-month/$', orders_last_month, name='orders-last-month'),
    re_path(r'^api/v1/order/plot/$', orders_plot, name='orders-plot'),
]
