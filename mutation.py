import graphene
from query import Employee

class CreateEmployee(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    employee = graphene.Field(lambda: Employee)

    def mutate(root, info, name):
        employee = Employee(name=name)
        ok = True
        return CreateEmployee(employee=employee, ok=ok)

class Mutations(graphene.ObjectType):
    create_employee = CreateEmployee.Field()