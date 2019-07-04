from django.contrib import admin
from .models import Categories,Image,Product,Video,Course,Payment,Enrolled,Sales

admin.site.register(Categories)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Payment)
admin.site.register(Enrolled)
admin.site.register(Sales)