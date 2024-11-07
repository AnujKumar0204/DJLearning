from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    print(request)
    return render(request,'index.html')
# def home(request):
#     print(request)
#     data = {
#         'message': 'Hello, world!',
#         'status': 'success'
#     }
#     return JsonResponse(data)