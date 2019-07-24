from rest_framework import serializers
from django.db.models import Avg
from . import models
from customer.models import User
from .youtube import upload_video


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Categories


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_id','id', 'product_id', 'first_name',
                  'email', 'comment')
        model = models.ProductReview


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id','id', 'product_id', 'first_name',
                  'email', 'rating')
        model = models.ProductRating

    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError(
            'Rating must be an integer between 1 to 5')


class ProductSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)
    images = serializers.StringRelatedField(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'user_id', 'product_name', 'product_description',
                  'product_price', 'product_made_of', 'categories', 'product_quantity',
                  'average_rating', 'images', 'reviews')
        model = models.Product

    def get_average_rating(self, obj):
        average = obj.rating.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
            return 0

        return round(average*2)/2

    def to_representation(self, value):
        temp = super().to_representation(value)
        cat = models.Categories.objects.get(id=temp['categories'])
        temp['category_name'] = cat.cat_name
        if 'is_list' in self.context:
            if self.context['is_list']:
                temp.pop('reviews')
                temp.pop('user_id')

        if 'is_created' in self.context:
            if self.context['is_created']:
                temp.pop('reviews')
                temp.pop('user_id')
        return temp


class ImageSerializer(serializers.ModelSerializer):
    # photo_url = serializers.SerializerMethodField()

    class Meta:
        fields = ('product_id', 'photo_url')
        model = models.Image


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = models.Cart


    def to_representation(self, value):
        temp = super().to_representation(value)
        obj = models.Product.objects.get(id = temp['product_id'])
        temp['product_name'] = obj.product_name
        temp['product_price'] = obj.product_price
        temp['product_quantity'] = obj.product_quantity
        img = models.Image.objects.filter(product_id = temp['product_id'])
        temp['img1'] = img[0].photo_url.url
        temp['img2'] = img[1].photo_url.url
        temp['img3'] = img[2].photo_url.url
        return temp

    


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id', 'product_id', 'product_name',
                  'quantity', 'mobile_no', 'price')
        model = models.Payment


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id', 'payment_id', 'sale_date')
        model = models.Sales


# Courses Serializer

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Questions


class TestSerializer(serializers.ModelSerializer):
    question = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = models.Test

    def to_representation(self, value):
        temp = super().to_representation(value)
        temp.pop('user_id')
        temp.pop('course_id')
        for item in temp['question']:
            item.pop('test_id')
            item.pop('id')
        return temp


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'course_id', 'title', 'video_url')
        model = models.Video

    def to_internal_value(self, data):
        temp = super().to_internal_value(data)
        return temp

    def to_representation(self, value):
        val = super().to_representation(value)
        print('-------------------')
        print(self.context)
        if 'is_enrolled' in self.context:
            if not self.context['is_enrolled']:
                val.pop('video_url')
        return val


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('video_id', 'user_id', 'course_id')
        model = models.WatchList


class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True,
                             context={'user': 'getUserType'})

    class Meta:
        fields = ('id', 'user_id', 'course_name', 'course_description', 'course_price',
                  'course_tools_required', 'videos', 'course_logo')
        model = models.Course

    def getUserType(self):
        return self.context['is_enrolled']

    def to_representation(self, value):
        val = super().to_representation(value)
        if 'is_list' in self.context:
            if self.context['is_list']:
                val.pop('videos')
        return val


class EnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Enrolled


class CoursePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.CoursePayment
