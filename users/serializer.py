from rest_framework.serializers import ModelSerializer
from users.models import User
from users.validators import validate_password


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         validators = [PasswordValidator]

from rest_framework import serializers
from users.models import User
from .validators import validate_password, validate_email


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            date_born=validated_data['date_born']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
