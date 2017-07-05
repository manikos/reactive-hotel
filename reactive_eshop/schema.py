from graphene import ObjectType, Schema

from product.schema import Query as product_Query


class Query(product_Query, ObjectType):
    pass


schema = Schema(query=Query, auto_camelcase=False)
