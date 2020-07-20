from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user
from django.shortcuts import get_object_or_404
from .serializers import userSerializer
from django.utils.decorators import method_decorator



def home(request):
    return render(request,'upload.html')


class MyView(APIView):
    
    def get(self,request):
        a=user.objects.all()
        serialize=userSerializer(a,many= True)
        return Response(serialize.data)

    def post(self,request):
        a=user.objects.all()[:2]
        serialize=userSerializer(a,many= True)
        return Response(serialize.data)

    def put(self,request):
        a=user.objects.all().order_by('-id')[:2]
        serialize=userSerializer(a,many= True)
        return Response(serialize.data,status=201)

class Acc(APIView):

    def post(self,request,name,password):
        u=user(name=name,password=password)
        u.save()
        a={
            "account":"created"
        }
        return Response(a)