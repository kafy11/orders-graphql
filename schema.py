import graphene
from query import Query
from mutations.mutation import Mutations

schema = graphene.Schema(query=Query, mutation=Mutations)