import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Product as ProductModel, Order as OrderModel

class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (relay.Node, )

class ProductConn(relay.Connection):
    class Meta:
        node = Product

class Order(SQLAlchemyObjectType):
    class Meta:
        model = OrderModel
        interfaces = (relay.Node, )

class OrderConn(relay.Connection):
    class Meta:
        node = Order

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    allRowsProduct = SQLAlchemyConnectionField(ProductConn)
    allRowsOrder = SQLAlchemyConnectionField(OrderConn)