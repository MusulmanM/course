from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Xush kelibsiz!")



urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/student/', include('student.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/lesson/', include('lesson.urls')),
    path('api/homework/', include('homework.urls')),
    path('api/course/', include('course.urls')),
    path('api/category/', include('category.urls')),
]
