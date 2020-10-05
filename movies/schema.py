import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django_graphql_movies.movies.models import Actor, Movie


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
