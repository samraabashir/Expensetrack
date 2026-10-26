from django.urls import path
from. import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login/seller/", views.seller_login, name="seller_login"),
    path("login/customer/", views.customer_login, name="customer_login"),
    path("seller/dashboard", views.seller_dashboard, name="seller_dashboard"),
    path("customer/dashboard", views.customer_dashboard, name="customer_dashboard"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("expense/add/", views.add_expense, name="add_expense"),
    path("expense/<int:expense_id>/edit/", views.edit_expense, name="edit_expense"),
    path("expense/<int:expense_id>/delete/", views.delete_expense, name="delete_expense"),
]