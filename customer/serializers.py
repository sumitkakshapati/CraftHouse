from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','first_name','last_name','email','date_of_birth','phoneno')
        model = models.User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id','zone','district','city','address')
        model = models.AddressBook
