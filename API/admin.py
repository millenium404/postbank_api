from django.contrib import admin
from .models import Client, Merchant, BankStaff, POS

admin.site.register(Client)
admin.site.register(Merchant)
admin.site.register(BankStaff)
admin.site.register(POS)
