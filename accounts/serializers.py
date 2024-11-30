
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User
from rest_framework import serializers
from django.db import models

class UserSerializer(ModelSerializer):
    class Meta :
        model  = User
        fields = "__all__"
        
    def save(self):
        user = User(**self.validated_data)
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user

class UserSerializer2(ModelSerializer):
    class Meta:
        model     = User
        fields    = ("id", "email", "username", "profile_pic", "mobile_number", "accepted_policy", "is_active","is_admin")

class UserSerializer1(ModelSerializer):
    class Meta :
        model   = User
        exclude = ("last_login","created_on","updated_on","password")

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    model = User

    def validate(self, value):
        if (self.initial_data["old_password"] and self.initial_data["new_password"]) :
            return value
        raise ValidationError(
            {
                "old_password": "This field may not be null.",
                "new_password": "This field may not be null.",
            }
        )

    def validate_old_password(self, old_password):
        print("in validate password")
        try : 
            user = self.context['request'].thisUser
        except : 
            raise serializers.ValidationError( "User Not Found")
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")
        return old_password
    
    def save(self):
        if (
            self.validated_data["old_password"]
            and self.validated_data["new_password"]
        ):
            user = self.context['request'].thisUser
            print("user")
            user.set_password(self.validated_data["new_password"])
            user.save()
        return user

class UserAdminSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = ('username','email','mobile_number','profile_pic',)


