from django.db import models

# 1. Биринчи Тур модели болушу керек
class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Турдун аталышы")
    description = models.TextField(verbose_name="Маалымат")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баасы")
    image = models.ImageField(upload_to='tours/', blank=True, null=True, verbose_name="Сүрөт")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. Заказ модели Турдан БӨЛӨК жана андан КИЙИН жазылышы керек
class Order(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE) # Эми Турду тааныйт
    full_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Заказ #{self.id} - {self.full_name}"