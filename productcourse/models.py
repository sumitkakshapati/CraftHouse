from django.db import models
from customer.models import User

class Categories(models.Model):
    cat_name = models.CharField(max_length = 100)
    cat_description = models.TextField()
    parent_cat_id = models.ForeignKey('self',on_delete = models.CASCADE,blank = True,null = True)

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE, default = 0)
    product_name = models.CharField(max_length = 100)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_made_of = models.CharField(max_length = 100)
    categories = models.ForeignKey(Categories,on_delete = models.CASCADE, default = 0)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class Image(models.Model):
    image = models.ImageField(upload_to ='products/')
    product_id = models.ForeignKey(Product,on_delete = models.CASCADE,default = 0)


class Course(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE, default = 0)
    course_name = models.CharField(max_length = 100)
    course_description = models.TextField()
    course_price = models.FloatField()
    categories = models.ForeignKey(Categories,on_delete = models.CASCADE, default = 0)

    def __str__(self):
        return self.course_name
    
class Video(models.Model):
    course_id = models.ForeignKey(Course,on_delete = models.CASCADE, default = 0)

