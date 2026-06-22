from django.http import HttpResponse
from rest_framework.decorators import api_view

def homepage(requets):
    return HttpResponse("Welcome to task manager")

@api_view(['POST'])
def subtraction(request):
    num1 = request.data.get("num1")
    num2 = request.data.get("num2")
    difference = num1 - num2
    return HttpResponse(f"The difference between {num1} and {num2} is {difference}")