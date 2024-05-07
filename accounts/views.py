from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from . serializers import UserSerializer

class AccountsView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        email = data['email']
        birth_date = data['birth_date']
        user = get_user_model().objects.create_user(username=username, password=password, email=email, birth_date=birth_date)
        return Response({'username': user.username, 'password': user.password, 'email': user.email, 'birth_date': user.birth_date}, status = 201)

class UserProfile(APIView):
    def get(self, request, username):
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)