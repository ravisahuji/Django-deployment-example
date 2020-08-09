from django.urls import path
from basic_app import views

# template tagging
app_name = 'basic_app'    # setting a global variable name



urlpatterns = [
    # path('other/', views.other, name= 'other'),
    path('other/', views.other, name= 'other_1'),
    path('relative/', views.relative, name= 'relative'),
]