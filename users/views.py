from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.

import jwt, datetime

class RegisterView(APIView):
    def post(self,request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        payload={
            "id": serializer.data['id'],
            "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret', algorithm='HS256').decode('utf-8')
        
        return Response(
            {   "id":serializer.data['id'],
                "token":token
                })


class LoginView(APIView):
    def post(self, request):
        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found')

        if  not user.check_password(password):
            raise  AuthenticationFailed('Wrong Password')
        payload = {
            "id": user.id ,
            "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow() }
        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')


        return Response({"message": "Success",
                            "id": user.id,
                         "token": token
                         })
