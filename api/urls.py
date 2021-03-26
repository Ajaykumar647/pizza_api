from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', views.product_list),
    path('get_orders/', views.get_all_data),
    path('delete_order/', views.delete_order),
    path('edit_order/', views.edit_order),

   
]