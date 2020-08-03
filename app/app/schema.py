import graphene 
import tracks.schema
import os

class Query(tracks.schema.Query, graphene.ObjectType):
    pass

class Mutation(tracks.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation )