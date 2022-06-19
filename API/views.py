from django.shortcuts import render
from rest_framework import authentication, generics, mixins, permissions
from .serializers import (ClientSerializer, MerchantSerializer,
    BankStaffSerializer, POSSerializer)
from .models import Client, Merchant, BankStaff, POS


class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        name = serializer.validated_data.get('name')
        email = serializer.validated_data.get('email')
        phone = serializer.validated_data.get('phone')
        card_number = serializer.validated_data.get('card_number')
        card_expires = serializer.validated_data.get('card_expires')
        serializer.save(
            username=username,
            password=password,
            name=name,
            email=email,
            phone=phone,
            card_number=card_number,
            card_expires=card_expires)


class MerchantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        name = serializer.validated_data.get('name')
        email = serializer.validated_data.get('email')
        phone = serializer.validated_data.get('phone')
        serializer.save(
            username=username,
            password=password,
            name=name,
            email=email,
            phone=phone)


class BankStaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = BankStaff.objects.all()
    serializer_class = BankStaffSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        name = serializer.validated_data.get('name')
        email = serializer.validated_data.get('email')
        serializer.save(
            username=username,
            password=password,
            name=name,
            email=email)


class POSListCreateAPIView(generics.ListCreateAPIView):
    queryset = POS.objects.all()
    serializer_class = POSSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        merchant = serializer.validated_data.get('merchant')
        serial_number = serializer.validated_data.get('serial_number')
        serializer.save(merchant=merchant, serial_number=serial_number)
