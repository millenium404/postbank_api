from rest_framework import serializers
from .models import Client, Merchant, BankStaff, POS


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'


class BankStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStaff
        fields = '__all__'


class POSSerializer(serializers.ModelSerializer):
    class Meta:
        model = POS
        fields = '__all__'
