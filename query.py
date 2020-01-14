import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, AGEncoded as AGEncodedModel, EquivalencyGroup as EquivalencyGroupModel


class AGEncoded(SQLAlchemyObjectType):
    class Meta:
        model = AGEncodedModel
        interfaces = (relay.Node, )

class AGEncodedConn(relay.Connection):
    class Meta:
        node = AGEncoded

class EquivalencyGroup(SQLAlchemyObjectType):
    class Meta:
        model = EquivalencyGroupModel
        interfaces = (relay.Node, )

class EquivalencyGroupConn(relay.Connection):
    class Meta:
        node = EquivalencyGroup

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    allRowsAGEncoded = SQLAlchemyConnectionField(AGEncodedConn)
    allRowsEquivalencyGroup = SQLAlchemyConnectionField(EquivalencyGroupConn)