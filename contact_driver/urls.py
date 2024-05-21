from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('contact_driver/', views.contact_us, name='contact_us'),
    path('products/', views.products, name='products'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('success/', views.success_page, name='success_page'),
    path('register/', views.registration_form, name='registration_form'),
    path('search/', views.search_page, name='search_page'),
    path('search-results/', views.search_results, name='search_results'),  # Update the URL pattern
    path('open_camera/', views.open_camera_view, name='open_camera'),
]
