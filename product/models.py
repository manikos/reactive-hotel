from django.db import models


class ShopItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at']

    def __str__(self):
        return self.name


class ProductCategory(ShopItem):
    pass

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class ProductAttribute(ShopItem):
    pass

    class Meta:
        verbose_name = 'Product Attribute'
        verbose_name_plural = 'Product Attributes'


class Product(ShopItem):
    categories = models.ManyToManyField(ProductCategory, related_name='products', related_query_name='products')
    attributes = models.ManyToManyField(ProductAttribute, related_name='attributes', related_query_name='attributes')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants')
    variation = models.ForeignKey(ProductAttribute, related_name='variations', blank=True, null=True)
    price = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variants'

    def __str__(self):
        return self.product.name
