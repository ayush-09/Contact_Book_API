from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Contact.as_view()),
    path('',views.ContactDetails.as_view()),
    path('update/<str:name>',views.ContactUpdate.as_view()),
    path('search/<str:name>',views.Search.as_view()),
]
