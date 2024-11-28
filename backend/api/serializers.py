from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def validate_password(self, value):
        if len(value) < 5:
            raise ValidationError("Password too weak.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("This email is already taken.")
        return value