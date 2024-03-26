from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('cod_confirm/', views.cod_confirm, name='cod_confirm'),
    path('cod_completed/', views.cod_completed, name='cod_completed'),
]