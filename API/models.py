from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    card_expires = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.username}'


class Merchant(models.Model):
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.username}'


class BankStaff(models.Model):
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.username}'


class POS(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    serial_number = models.CharField(
        max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.serial_number} - {self.merchant}'
