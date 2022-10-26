import graphene
from graphene_django import DjangoObjectType
from .models import Category, Book, Grocery


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','title')


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)

    def resolve_categories(self, root, info, **kwargs):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
