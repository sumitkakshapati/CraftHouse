from django.db import models
from customer.models import User
from django.utils import timezone


class Categories(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_description = models.TextField()
    cat_logo = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.cat_name

# Products Part


class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    product_name = models.CharField(max_length=100)
    product_made_of = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    categories = models.ForeignKey(
        Categories, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name


class Image(models.Model):
    photo_url = models.ImageField(upload_to='products/')
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=0, related_name='images')

    def __str__(self):
        return str(self.photo_url)


class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0,)
    quantity = models.IntegerField(default = 0)

    class Meta:
        unique_together = ('user_id','product_id')


class ProductRating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0,)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=0, related_name='rating')
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rating = models.IntegerField()

class ProductReview(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0,)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=0, related_name='reviews')
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=255)



class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=0)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    mobile_no = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.0)


class Sales(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(default=timezone.now)


# Courses Part


class Course(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_price = models.FloatField()
    course_tools_required = models.TextField(default='None')
    created_at = models.DateTimeField(default=timezone.now)
    course_logo = models.ImageField(
        upload_to='courses/', null=True, blank=True)

    def __str__(self):
        return self.course_name


class Test(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)


class Questions(models.Model):
    ANSWER_OPTIONS = (
        ('1', 'option1'),
        ('2', 'option2'),
        ('3', 'option3'),
        ('4', 'option4')
    )
    test_id = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name='question')
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(
        max_length=2, choices=ANSWER_OPTIONS, default='1')


class Video(models.Model):
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=0, related_name='videos')
    title = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, null=False, blank=False)

    REQUIRED_FIELD = ['course_id', 'user_id', 'name', 'video_url']


class WatchList(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE, default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)

    class Meta:
        unique_together = ('video_id', 'user_id', 'course_id')


class CoursePayment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    course_name = models.CharField(max_length=255)
    price = models.FloatField()


class Enrolled(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    payment_id = models.ForeignKey(
        CoursePayment, on_delete=models.CASCADE, default=0)
    enrolled_date = models.DateTimeField(default=timezone.now)


class Report(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    total_question = models.IntegerField(default=0)
    score = models.IntegerField(default=0)


class Progress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    progress_percentage = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('user_id', 'course_id')
