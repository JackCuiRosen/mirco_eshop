from django.db import models


# Create your models here.

class Product(models.Model):
    """
    商品模型
    """
    name = models.CharField(max_length=100, verbose_name="商品名称")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品价格")
    stock = models.IntegerField(verbose_name="商品库存")
    keywords = models.CharField(max_length=100, verbose_name="商品关键字")
    description = models.TextField(verbose_name="商品描述")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
