from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from App1.models import User, UserProfile
from App1.serializers import UserSerializer, UserAmendSerializer


class UserMessageView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):

        return JsonResponse(request.data)

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


class UserAmendView(RetrieveUpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserAmendSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=id)[0]

        user_amend_serializer = UserAmendSerializer(user)
        return JsonResponse(user_amend_serializer.data)

    def put(self, request,  *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):

        # id = request.data.get("id")
        u_phone = request.data.get("u_phone")
        u_username = request.data.get("u_username")
        u_sex = request.data.get("u_sex")
        u_birth_year = request.data.get("u_birth_year")
        u_location = request.data.get("u_location")
        u_hobby = request.data.get("u_hobby")
        u_instructions = request.data.get("u_instructions")

        user = User.objects.filter(id=id)[0]
        user.u_phone = u_phone or user.u_username
        user.u_username = u_username or user.u_username
        user.u_sex = u_sex or user.u_sex
        user.u_birth_year = u_birth_year or user.u_birth_year
        user.u_location = u_location or user.u_location
        user.u_hobby = u_hobby or user.u_hobby
        user.u_instructions = u_instructions or user.u_instructions
        user.save()

        user_amend_serializer = UserAmendSerializer(user)

        return JsonResponse(user_amend_serializer.data)