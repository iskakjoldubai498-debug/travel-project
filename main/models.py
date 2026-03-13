from django.db import models

# 1. ТУР МОДЕЛИ (Биринчи келиши керек)
class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Турдун аталышы")
    description = models.TextField(verbose_name="Маалымат")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баасы")
    image = models.ImageField(upload_to='tours/', blank=True, null=True, verbose_name="Сүрөт")
    is_active = models.BooleanField(default=True, verbose_name="Активдүү")
    order = models.IntegerField(default=0, verbose_name="Ирет номери")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. ЗАКАЗ МОДЕЛИ (Турдан кийин жана СӨЗСҮЗ четинен башталат)
class Order(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        verbose_name="Тур",
        related_name='tour_orders'
    )
    full_name = models.CharField(max_length=255, verbose_name="Кардардын аты-жөнү")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    status = models.CharField(max_length=20, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Заказ #{self.id} - {self.full_name}"