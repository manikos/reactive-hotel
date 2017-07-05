import graphene
# from graphene import AbstractType, List, ObjectType
from graphene_django.types import DjangoObjectType

from .models import ProductCategory, Product, ProductAttribute, ProductVariant


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory


class ProductAttributeType(DjangoObjectType):
    class Meta:
        model = ProductAttribute


class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant


class ProductType(DjangoObjectType):
    """
    Implies that all fields of the Product model will be queried. If I want to exclude some fields from
    being queried (like creation/update date) I have to define them explicit in the "exclude_fields" list.
    This type describes all the fields that the Product model has and also some extra fields (the M2M relations),
    categories and attributes, which are described here explicit and are of different type each.
    """
    # name = 'Product Type'
    # description = '....'

    categories = graphene.List(ProductCategoryType)
    attributes = graphene.List(ProductAttributeType)

    class Meta:
        model = Product
        # exclude_fields = ['updated_at']

    def resolve_categories(self, args, context, info):
        """
        "self" is the Product instance, type(self) is the model class (described in the current Meta), that is
        product.models.Product
        :param args:
        :return:
        """
        return self.categories.all()

    def resolve_attributes(self, args, context, info):
        """
        "self" is the Product instance, type(self) is the model class (described in the current Meta), that is
        product.models.Product
        :param args:
        :return:
        """
        return self.attributes.all()


class Query(graphene.AbstractType):
    """
    Our API has a Query (this class, the entry point) and the Query has some Endpoints ("all_products", "product" etc )
    and the returned type of each Endpoint is a graphene.??? type.
    For example, if someone queries for "all_products", then it will return a list of ProductType items.
    Each item in this list is a ProductType.
    If someone, queries for "product", it must take an argument (id, of type "string") and it will return a specific
    ProductType field.
    """
    product = graphene.Field(ProductType, id=graphene.String())
    products = graphene.List(ProductType)
    categories = graphene.List(ProductCategoryType)
    # all_variants = List(ProductVariantType)

    def resolve_product(self, args, context, info):
        pk = args.get('id')
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def resolve_products(self, args, context, info):
        return Product.objects.all()

    def resolve_categories(self, args, context, info):
        return ProductCategory.objects.all()
