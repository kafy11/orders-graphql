import graphene
from mutations.product import CreateProduct, UpdateProduct, DeleteProduct
from mutations.order import CreateOrder, UpdateOrder, DeleteOrder

class Mutations(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()