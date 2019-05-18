from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id', 'product_name', 'product_description',
                  'product_price', 'product_made_of', 'categories', 'product_quantity')
        model = models.Product


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id', 'course_name', 'course_description', 'course_price', 'categories')
        model = models.Course
