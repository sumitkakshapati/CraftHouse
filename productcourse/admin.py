from django.contrib import admin
from .models import Categories,Image,Product,Video,Course,Payment,Enrolled,Sales,Test,Questions,Cart,ProductRating,ProductReview,CourseRating,CourseReview,Progress,Report,WatchList

admin.site.register(Categories)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Payment)
admin.site.register(Enrolled)
admin.site.register(Sales)
admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(Cart)
admin.site.register(ProductRating)
admin.site.register(ProductReview)
admin.site.register(CourseRating)
admin.site.register(CourseReview)
admin.site.register(Progress)
admin.site.register(Report)
admin.site.register(WatchList)
admin.site.site_header="CRAFT HOUSE ADMIN PANEL"

