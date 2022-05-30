from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list_view, name='product-list'),
    path('create/', views.product_create_view, name='product-create'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_destroy_view, name='product-delete'),

    # path('', views.product_mixin_view),
    # path('create/', views.product_mixin_view),
    # path('<int:pk>/', views.product_mixin_view),
]
