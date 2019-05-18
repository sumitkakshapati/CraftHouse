from django.db import models
from tastypie.resources import ModelResource
from customer.models import User
from tastypie.authorization import Authorization

class CustomerResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        authorization = Authorization()
