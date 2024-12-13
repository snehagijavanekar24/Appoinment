from django.contrib import admin
from django.urls import path,include
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/',booking, name='booking'),
    path('delete/<id>/', delete_booking, name='delete_booking'),
    path('update/<id>/', update_booking, name='update_booking'),

]