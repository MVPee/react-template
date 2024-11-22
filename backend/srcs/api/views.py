from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer

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

class View():

    @api_view(['GET'])
    def home(request):
        content = render(request, 'home.html', context={}).content.decode("utf-8")
        return Response({"html": content}, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def about(request):
        content = render(request, 'about.html', context={}).content.decode("utf-8")
        return Response({"html": content}, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def contact(request):
        content = render(request, 'contact.html', context={}).content.decode("utf-8")
        return Response({"html": content}, status=status.HTTP_200_OK)
