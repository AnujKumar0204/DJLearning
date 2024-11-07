from rest_framework import routers, serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import UserAccount, Post
from .serilazers import UserAccountSerializer, PostSerializer, PostSerializerMini

# User Viewset
class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    
# Post Viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# User Creation
class CreateUserViewSet(APIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    def post(self,request):
        # import ipdb
        # ipdb.set_trace()
        body=request.data
        serialized_data=UserAccountSerializer(data=body)
        
        if not serialized_data.is_valid():
            return Response({'msg': "Unable To Create User"},status=status.HTTP_400_BAD_REQUEST)
            
        firstname=body.get('firstname')
        lastname=body.get('lastname')

        user,_ucreated=UserAccount.objects.get_or_create(firstname=firstname, lastname=lastname)
        
        return Response({'msg': "User Created Successfully"},status=status.HTTP_201_CREATED)

# User Posts
class UserPostsViewSet(APIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    def get(self,request,user_id):
        user_obj=UserAccount.objects.get(id=user_id)
        user_posts=user_obj.post_set.all()

        user_posts_serilier=PostSerializerMini(user_posts,many=True)
        user_serilier=UserAccountSerializer(user_obj)

        data={
            'user': user_serilier.data,
            'posts':user_posts_serilier.data
        }
        
        return Response(data)

        