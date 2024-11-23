from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
import os

API_KEY = os.getenv('API_KEY')

"""
    How to use the API_KEY for somes privates API (micro service)

    #*      import requests

    #*      API_KEY = os.getenv('API_KEY')
    #*      response = requests.get(API_URL, headers={"X-API-Key": API_KEY})
"""

"""
    #*      @api_view(['GET'])
    #*      def get_...(request):
    #*      if request.headers.get('X-API-Key') != API_KEY:
    #*          return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
    #*      else
    #*          ...
"""

@api_view(['GET'])
def get_user(request, pk):
    try:
        users = User.objects.get(pk=pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User(
            username=serializer.validated_data['username'],
            email=serializer.validated_data.get('email'),
        )
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class View(APIView):

    content = None
    status = status.HTTP_200_OK
    auth_required = False

    def get(self, request):
        if self.auth_required and not request.user.is_authenticated:
            self.status = status.HTTP_403_FORBIDDEN
            self.content = render(
                request, 'home.html',
                context={"error_message": "You need to be authenticated to have access to this page"}
            ).content.decode("utf-8")
        return Response({"html": self.content}, self.status)


class home(View):

    auth_required = False

    def get(self, request):
        self.content = render(
            request,
            'home.html',
            context={}
        ).content.decode("utf-8")
        return super().get(request)    


class about(View):

    auth_required = False

    def get(self, request):
        self.content = render(
            request,
            'about.html',
            context={}
        ).content.decode("utf-8")
        return super().get(request)


class contact(View):

    auth_required = True

    def get(self, request):
        self.content = render(
            request,
            'contact.html',
            context={}
        ).content.decode("utf-8")
        return super().get(request)
