import graphene
from graphene_django.types import DjangoObjectType
from account.models import UserAccount, Post

# Define a GraphQL type for your model
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"
        
        
class UserAccountType(DjangoObjectType):
    post = graphene.Field(PostType, id=graphene.Int())
    posts = graphene.List(
        PostType,
        start=graphene.Int(default_value=0),  # Default start index
        end=graphene.Int(default_value=None),  # Default end index (no limit)
    )

    class Meta:
        model = UserAccount
        fields = "__all__"
        
    def resolve_post(self, info, id):
        return self.post_set.get(pk=id)  # Assuming a reverse relationship `post_set`
    
    def resolve_posts(self, info, start, end):
        posts = self.post_set.all()  # Adjust if your related_name is different
        return posts[start:end]  # Slice the queryset based on start and end

# Define your queries
class Query(graphene.ObjectType):
    
    all_user = graphene.List(UserAccountType)
    user = graphene.Field(UserAccountType, id=graphene.Int())
    
    def resolve_all_user(self, info):
        return UserAccount.objects.all()

    def resolve_user(self, info, id):
        try:
            return UserAccount.objects.get(pk=id)
        except UserAccount.DoesNotExist:
            return None
    
    post = graphene.Field(PostType, id=graphene.Int())
    
    def resolve_post(self, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return None

        

# Create the schema
schema = graphene.Schema(query=Query)
