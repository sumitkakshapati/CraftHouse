from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from . import models
from . import serializers



#List View For User

# class ListUser(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer

    #def get(self, request, format = None):
     #   users = models.User.objects.all()
      #  serializer = serializers.UserSerialzer(users,many = True)
       # return Response(serializer.data)

    #def post(self, request, format = None):
     #   serializer = serializers.UserSerialzer(data = request.data)
      #  serializer.is_valid(raise_exception = True)
       # serializer.save()
        #return Response(serializer.data,status=status.HTTP_201_CREATED)


#Update , delete and retrieve User

class RetriveUpdateUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

# create Address

class CreateAddress(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.User.objects.all()
    serializer_class = serializers.AddressSerializer
    
    def perform_create(self, serializer):
        temp = self.request.META.get('HTTP_AUTHORIZATION');
        token_id = temp.split()[1]

        user_id = Token.objects.get(key = token_id).user_id

        print('-----------------------------')
        print(user_id)
        print('-----------------------------')
        print(self.request.data['user_id'])
        #print(type(self.args.))
        if (self.request.data['user_id'] == str(user_id)):
            serializer.save()
        else:
            raise ValidationError({'Detail': 'Token and user id doesnot Match'})
            


#Update , Delete and retrieve Address

class RetrieveUpdateAddress(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.User.objects.all()
    serializers_class = serializers.AddressSerializer
