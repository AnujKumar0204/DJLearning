from rest_framework import routers, serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import UserAccount, Post
from .serilazers import UserAccountSerializer, PostSerializer, PostSerializerMini
from middleware.auth import auth
import jwt

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
    
    # create new user with no validation
    # def post(self,request):
    #     # import ipdb
    #     # ipdb.set_trace()
    #     body=request.data
    #     serialized_data=UserAccountSerializer(data=body)
        
    #     if not serialized_data.is_valid():
    #         return Response({'msg': "Unable To Create User"},status=status.HTTP_400_BAD_REQUEST)
            
    #     firstname=body.get('firstname')
    #     lastname=body.get('lastname')

    #     user,_ucreated=UserAccount.objects.get_or_create(firstname=firstname, lastname=lastname)
        
    #     return Response({'msg': "User Created Successfully"},status=status.HTTP_201_CREATED)
    
    # create new user with password and validation
    def post(self,request):
        
        
        # import ipdb
        # ipdb.set_trace()
        body=request.data
        serialized_data=UserAccountSerializer(data=body)
        
        if not serialized_data.is_valid():
            return Response({'msg': "Unable To Create User", 'error': serialized_data.errors},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user=UserAccount.objects.filter(username=body['username'])
            if user.exists():
                return Response({'msg': "Username already exist", },status=status.HTTP_400_BAD_REQUEST)
            
            user=UserAccount.objects.create(**body)
            user.set_password(body['password'])
            user.save()
            
            serialized_user=UserAccountSerializer(user).data
            
            return Response({'msg': "User Created Successfully", 'result': serialized_user},status=status.HTTP_201_CREATED)
        
        except InterruptedError as e:
                print("Fetal Error", e)
    
class LoginUserViewSet(APIView):
    
    # create new user with password and validation
    # @auth
    def post(self,request):
        # import ipdb
        # ipdb.set_trace()
        body=request.data
        # token = request.headers
        # print(token)
        
        try:
            user=UserAccount.objects.filter(username=body['username'])
            if not user.exists():
                return Response({'msg': "No User Found", },status=status.HTTP_400_BAD_REQUEST)
            
            # user=UserAccount.objects.create(**body)
            user=UserAccount.objects.get(username=body['username'])
            valid_pass=user.check_password(body['password'])

            if not valid_pass:
                return Response({'msg': "Username or password does not match", },status=status.HTTP_400_BAD_REQUEST)
            
            serialized_user=UserAccountSerializer(user).data
            
            access_token = jwt.encode(serialized_user, 'MySecretKey', algorithm='HS256')
            
            data={
                'msg': "Login Successful", 
                'result': {
                    'access_token': access_token,
                    'user': serialized_user
                }
            }
            
            return Response(data,status=200)
        
        except InterruptedError as e:
                print("Fetal Error", e)

class UserDetailsViewSet(APIView):
    
    # create new user with password and validation
    @auth
    def get(self, request, user_id):
        # import ipdb
        # ipdb.set_trace()
        # body=request.data
        # token = request.headers
        # print(token)
        
        try:
            
            user=UserAccount.objects.filter(id=user_id)
            if not user.exists():
                return Response({'msg': "Invalid User Id", },status=status.HTTP_400_BAD_REQUEST)
            
            user=UserAccount.objects.get(id=user_id)
            serialized_user=UserAccountSerializer(user).data
            
            return Response({'msg': 'User Details Fetch successfuly', 'result': serialized_user},status=200)
        
        except InterruptedError as e:
                print("Fetal Error", e)
                    

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

        