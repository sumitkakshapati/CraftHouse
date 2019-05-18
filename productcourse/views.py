from rest_framework import generics
from . import models
from rest_framework.permissions import IsAuthenticated,AllowAny
from . import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError,PermissionDenied
from customer.models import User
from django.http import Http404

class CreateProduct(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):
        temp = self.request.META.get('HTTP_AUTHORIZATION');
        token_id = temp.split()[1]

        user_id = Token.objects.get(key = token_id).user_id
        is_seller = User.objects.get(id = user_id).is_seller

        if (self.request.data['user_id'] == str(user_id)):
            if (is_seller):
                serializer.save()
            else:
                raise PermissionDenied({'Detail': 'User cannot upload the product'})    
        else:
            raise ValidationError({'Detail': 'Token and user id doesnot Match'})

class ListAllProduct(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ListProductsByCategories(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        try:
            category_id = models.Categories.objects.get(cat_name__iexact = self.kwargs['category']).id
        except models.Categories.DoesNotExist:
            raise Http404({'details':'Category Not Found'})
        query = models.Product.objects.filter(categories = category_id)
        return query


class SearchProduct(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = models.Product.objects.filter(product_name__icontains = self.kwargs['keyword'])
        return query

        
