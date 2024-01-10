from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Users


# Create your views here.
class Login(APIView):
    def post(self, request):
        schema= {
            "email": {'type': 'string', 'required': True, 'empty': False},
        }

        if Users.objects.filter(email=request.data['email']).exists():
            return render(request, 'user/register.html', {'form': form})
        return Response('USER DOES NOT EXISTS', status=status.HTTP_200_OK)
