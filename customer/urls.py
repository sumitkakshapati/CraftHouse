from django.urls import path

from . import views

urlpatterns = [
    # path('',views.ListUser.as_view(),name = 'user_list'),
    path('<int:pk>',views.RetriveUpdateUser.as_view(),name = 'user_detail'),
    path('address/',views.CreateAddress.as_view(),name = 'address_create'),
    path('address/<int:pk>/',views.RetrieveUpdateAddress.as_view(),name='address_detail'),
]


