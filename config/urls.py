from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/student/', include('student.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/lesson/', include('lesson.urls')),
    path('api/homework/', include('homework.urls')),
    path('api/course/', include('course.urls')),
    path('api/category/', include('category.urls')),
]
