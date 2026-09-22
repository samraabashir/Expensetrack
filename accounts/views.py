from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    return render(request, "accounts/login.html")




def seller_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == "SELLER":
            login(request, user)
            return redirect("seller_dashboard")
        return render(request, "accounts/seller_login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "accounts/seller_login.html")

def seller_dashboard(request):

    return render(request, "accounts/seller_dashboard.html")



def customer_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == "CUSTOMER":
            login(request, user)
            return redirect("customer_dashboard")

        return render(request, "accounts/customer_login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "accounts/customer_login.html")


def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")