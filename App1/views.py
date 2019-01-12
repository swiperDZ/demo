from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from App1.models import User, UserProfile
from App1.serializers import UserSerializer


class HelloView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):

        return Response('Hello django')

    def post(self, request, *args, **kwargs):

        u_phone = request.data.get("u_phone")
        u_username = request.data.get("u_username")
        u_sex = request.data.get("u_sex")
        u_birth_year = request.data.get("u_birth_year") or None
        u_location = request.data.get("u_location") or None
        u_hobby = request.data.get("u_hobby") or None
        u_instructions = request.data.get("u_instructions") or None

        user = User()
        user.u_phone = u_phone
        user.u_username = u_username
        user.u_sex = u_sex
        user.u_birth_year = u_birth_year
        user.u_location = u_location
        user.u_hobby = u_hobby
        user.u_instructions = u_instructions
        user.save()

        user_serializer = UserSerializer(user)

        return JsonResponse(user_serializer.data)
