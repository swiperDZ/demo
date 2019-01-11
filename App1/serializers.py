
from rest_framework import serializers

from App1.models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):

    u_phone = serializers.CharField(required=True, max_length=16)
    u_username = serializers.CharField(required=True, max_length=32)
    u_sex = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = ("u_username", "u_sex" "u_birth_year")
#       "u_location", "u_hobby", "u_instructions"


class UserProfileSerializer(serializers.ModelSerializer):
    p_user_id = serializers.IntegerField(required=True)
    p_dating_sex = serializers.BooleanField(required=True)
    p_location = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = UserProfile
        fields = ("p_user_id", "p_location", "p_dating_sex")

