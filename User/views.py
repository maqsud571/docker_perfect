from django.shortcuts import render
from .models import UserModel
from rest_framework import status
from .serializers import UserSRL
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#
class Register(APIView):
    @swagger_auto_schema(request_body=UserSRL)
    def post(self,request):
        serializer = UserSRL(data=request.data)
        if serializer.is_valid():
            nimagap = serializer.save()
            access = AccessToken.for_user(nimagap)
            refresh = RefreshToken.for_user(nimagap)

            return Response({"data":serializer.data,"access": str(access),"refresh": str(refresh)})
        else:
            return Response(serializer.errors,status=400)


class Login(APIView):
    @swagger_auto_schema(request_body=UserSRL)
    def post(self,request):
        name = request.data.get("name")
        password = request.data.get("password")
        user = UserModel.objects.all().filter(name=name,password=password).first()
        if user:
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            serializer = UserSRL(user)
            return Response({"Data":serializer.data,"access":str(access),"refresh":str(refresh)})
        else:
            return Response("Bunday user mavjud emas")
        
class Logaut(APIView):
    def get(self,request,name):
        user = UserModel.objects.all().filter(name=name).first()
        if user:
            refresh = RefreshToken.for_user(user)
            serializer = UserSRL(user)
            return Response ({"Data":serializer.data,"refresh":str(refresh)})
        else:
            return Response({"MSG":"kalamush bunday USER yo'q"})
        


class AllUser(APIView):
    def get(self,request):
        queryset = UserModel.objects.all()  # Corrected 'object == objects
        serializer = UserSRL(queryset ,many=True)
        return Response(serializer.data)

