from rest_framework import routers, serializers, viewsets
from account.models import UserAccount, Post

# Serializers define the API representation.
class PostSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description']

class UserAccountSerializer(serializers.ModelSerializer):
    # posts=serializers.SerializerMethodField()
    class Meta:
        model = UserAccount
        fields = ['id', 'firstname', 'lastname', 'username']
        
    # def get_posts(self,obj):
    #     posts=obj.post_set.all()
    #     return PostSerializerMini(posts,many=True).data

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    # user=UserAccountSerializer()
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description']

# 
