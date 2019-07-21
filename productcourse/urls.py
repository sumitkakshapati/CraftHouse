from django.urls import path

from . import views

urlpatterns = [
    #Products
    path('products/categories/',views.ListCategories.as_view(),name = 'list_categories'),
    path('products/add/', views.CreateProduct.as_view(), name='add_product'),
    path('products/', views.ListAllProduct.as_view(), name='list_product'),
    path('products/<int:pk>/',views.ProductDetail.as_view(),name='product_details'),
    path('products/update/<int:pk>/',views.ProductUpdate.as_view(), name = 'product_update'),
    path('products/delete/<int:pk>/',views.ProductDelete.as_view(), name = 'product_delete'),
    path('products/categories/<str:category>/',
         views.ListProductsByCategories.as_view(), name='list_product_by_category'),
    path('products/search/<str:keyword>/',views.SearchProduct.as_view(),name = 'search_product'),
    path('image/',views.SearchImage.as_view(),name = 'search_image'),
    path('image/add',views.CreateImage.as_view()),
    path('products/review/add/',views.CreateProductReview.as_view()),
    path('sale/',views.CreateSales.as_view(),name = 'manage_sales'),
    path('payment/product/',views.CreatePayment.as_view(),name = 'payment'),
    
    #Courses
    
    path('courses/add/',views.CreateCourse.as_view(),name = 'add_courses'),
    path('video/add/',views.CreateVideo.as_view(),name = 'add_video'),
    path('video/add/watchlist/',views.CreateWatchList.as_view(),name = 'add_watchList'),
    path('courses/',views.ListCourse.as_view(),name='list_courses'),
    path('courses/<int:pk>/',views.CourseDetail.as_view(),name='course_detail'),
    path('courses/update/<int:pk>/',views.CourseUpdate.as_view(), name = 'course_update'),
    path('courses/delete/<int:pk>/',views.CourseDelete.as_view(), name = 'course_delete'),
    path('courses/payment/',views.CreateCoursePayment.as_view(),name='course_payment'),
    path('courses/createtest/',views.CreateTest.as_view(),name = 'create_test'),
    path('courses/<pk>/taketest/',views.RetrieveTest.as_view(),name = 'detail_test'),
    path('courses/createquestion/',views.CreateQuestions.as_view(),name = 'create_questions'),
]
