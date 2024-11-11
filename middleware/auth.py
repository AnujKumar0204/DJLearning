from functools import wraps
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response

def auth(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        # Run your function here
        # For example, log the request or modify the data:
        token = request.headers.get('Authorization', False)
        if not token:
            return Response({'err': "Authorization Required", },status=status.HTTP_400_BAD_REQUEST)
        
        # You can add logic here, like validating the request or doing logging
        # If you want to prevent the view from being called, you can return a response here:
        # return JsonResponse({'error': 'some error'}, status=400)
        
        return func(self, request, *args, **kwargs)
    return wrapper