import graphene
from query import Product
from models import db_session, Product as ProductModel

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

    def mutate(root, info, name, price):
        product = ProductModel(name=name, price=price)
        db_session.add(product)
        db_session.commit()

        ok = True
        return CreateProduct(product=product, ok=ok)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        productId = graphene.Int(required=True)
        name = graphene.String(required=False)
        price = graphene.Float(required=False)

    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

    def mutate(root, info, productId, name = False, price = False):
        product = db_session.query(ProductModel).filter(ProductModel.productId == productId).first()

        if(name != False):
            product.name = name
        
        if(price != False):
            product.price = price 
        
        db_session.commit()

        ok = True
        return UpdateProduct(product=product, ok=ok)

class DeleteProduct(graphene.Mutation):
    class Arguments:
        productId = graphene.Int(required=True)
    
    ok = graphene.Boolean()

    def mutate(root, info, productId):
        product = db_session.query(ProductModel).filter(ProductModel.productId == productId).first()
        db_session.delete(product)
        db_session.commit()

        ok = True
        return DeleteProduct(ok=ok)