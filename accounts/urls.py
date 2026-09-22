from django.urls import path
from. import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login/seller/", views.seller_login, name="seller_login"),
    path("login/customer/", views.customer_login, name="customer_login"),
    path("seller/dashboard", views.seller_dashboard, name="seller_dashboard"),
    path("customer/dashboard", views.customer_dashboard, name="customer_dashboard"),
]