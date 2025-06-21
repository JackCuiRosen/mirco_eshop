from django.db import models

from apps.products.models import Product


# Create your models here.


class Order(models.Model):
    """
    订单模型
    """
    STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成'),
        (6, '已取消'),
    )
    order_id = models.CharField(max_length=32, verbose_name="订单编号")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="订单状态")
    notes = models.TextField(verbose_name="订单备注")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"


class OrderDetail(models.Model):
    """
    订单详情模型
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="所属订单")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")
    quantity = models.IntegerField(verbose_name="商品数量")
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品价格")

    def __str__(self):
        return f"{self.order.order_id} : {self.product.name} x {self.quantity}"

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"
        unique_together = ('order', 'product')
