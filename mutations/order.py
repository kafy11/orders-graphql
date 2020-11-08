import graphene
from query import Order
from models import db_session, Order as OrderModel

class CreateOrder(graphene.Mutation):
    class Arguments:
        productId = graphene.Int(required=True)
        qty = graphene.Int(required=True)

    ok = graphene.Boolean()
    order = graphene.Field(lambda: Order)

    def mutate(root, info, productId, qty):
        order = OrderModel(qty=qty, productId=productId)
        db_session.add(order)
        db_session.commit()

        ok = True
        return CreateOrder(order=order, ok=ok)

class UpdateOrder(graphene.Mutation):
    class Arguments:
        orderId = graphene.Int(required=True)
        productId = graphene.Int(required=False)
        qty = graphene.Int(required=False)

    ok = graphene.Boolean()
    order = graphene.Field(lambda: Order)

    def mutate(root, info, orderId, productId = False, qty = False):
        order = db_session.query(OrderModel).filter(OrderModel.orderId == orderId).first()

        if(productId != False):
            order.productId = productId
        
        if(qty != False):
            order.qty = qty 
        
        db_session.commit()

        ok = True
        return UpdateOrder(order=order, ok=ok)

class DeleteOrder(graphene.Mutation):
    class Arguments:
        orderId = graphene.Int(required=True)
    
    ok = graphene.Boolean()

    def mutate(root, info, orderId):
        order = db_session.query(OrderModel).filter(OrderModel.orderId == orderId).first()
        db_session.delete(order)
        db_session.commit()

        ok = True
        return DeleteOrder(ok=ok)