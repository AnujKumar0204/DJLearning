from functools import wraps
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from account.models import UserAccount
import jwt

def auth(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        # Run your function here
        # For example, log the request or modify the data:
        try:
            
            token = request.headers.get('Authorization', False)
            if not token:
                return Response({'err': "Authorization Required", },status=status.HTTP_400_BAD_REQUEST)

            token_data = jwt.decode(token, 'MySecretKey', 'HS256')

            user=UserAccount.objects.filter(id=token_data['id'])
            if not user.exists():
                return Response({'msg': "Invalid Token", },status=status.HTTP_400_BAD_REQUEST)
        
        except InterruptedError as e:
                print("Fetal Error", e)
        
        # You can add logic here, like validating the request or doing logging
        # If you want to prevent the view from being called, you can return a response here:
        # return JsonResponse({'error': 'some error'}, status=400)
        
        return func(self, request, *args, **kwargs)
    return wrapper