from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from . models import User, Expense


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
        expenses = Expense.objects.filter(seller=request.user)

        return render(request, "accounts/seller_dashboard.html",{
         "expenses": expenses
    })

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


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")


        if User.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html", {
                "error": "Username already exists. Please choose another username."
            })

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        login(request, user)

        if role == "SELLER":
            return redirect("seller_dashboard")
        else:
            return redirect("customer_dashboard")

    return render(request, "accounts/signup.html")


def logout_view(request):
    logout(request)
    return redirect("login")

def add_expense(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        date = request.POST.get("date")
        description = request.POST.get("description")

        Expense.objects.create(
            seller=request.user,
            name=name,
            amount=amount,
            category=category,
            date=date,
            description=description
        )

        return redirect("seller_dashboard")

    return render(request, "accounts/add_expense.html")

def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)

    if request.method == "POST":
        expense.name = request.POST.get("name")
        expense.amount = request.POST.get("amount")
        expense.category = request.POST.get("category")
        expense.date = request.POST.get("date")
        expense.description = request.POST.get("description")

        expense.save()

        return redirect("seller_dashboard")

    return render(request, "accounts/edit_expense.html", {
        "expense": expense
    })

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)

    if request.method == "POST":
        expense.delete()
        return redirect("seller_dashboard")

    return render(request, "accounts/delete_expense.html", {
        "expense": expense
    })