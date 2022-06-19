from django.contrib import admin
from django.urls import path
from API.views import (
    ClientListCreateAPIView,
    MerchantListCreateAPIView,
    BankStaffListCreateAPIView,
    POSListCreateAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', ClientListCreateAPIView.as_view()),
    path('merchants/', MerchantListCreateAPIView.as_view()),
    path('staff/', BankStaffListCreateAPIView.as_view()),
    path('pos/', POSListCreateAPIView.as_view()),
]
