from django.urls import path

from . import views

urlpatterns = [
    path('products/add/', views.CreateProduct.as_view(), name='add_product'),
    path('products/', views.ListAllProduct.as_view(), name='list_product'),
    path('products/categories/<str:category>',
         views.ListProductsByCategories.as_view(), name='list_product_by_category'),
    path('products/search/<str:keyword>',views.SearchProduct.as_view(),name = 'search_product')
    # path('address/',views.CreateAddress.as_view(),name = 'address_create'),
    # path('address/<int:pk>',views.RetrieveUpdateAddress.as_view(),name='address_detail'),
]
