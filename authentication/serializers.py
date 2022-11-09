from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True, validators=[validate_password], write_only=True
    )
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["username", "email", "password", "password2"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields don't match"})
        return data

    def create(self, validated_data):
        user = settings.AUTH_USER_MODEL.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        return user