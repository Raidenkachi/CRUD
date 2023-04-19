from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello,name='hello'),
    path('image/', views.image, name='image'),
    path('bgimage/', views.background, name='background'),
    path('members/', views.members, name='members'),
    path('toto/', views.student, name='student'),
    path('otot/', views.sacarstic, name='sacarstic'),
    path('seshon/', views.setsession, name='setsession'),
    path('sesson/', views.getsession, name='getsession'),
    path('notice/', views.animal, name='animal'),
]
