
import queue
from django.shortcuts import redirect, render
from .models import *
from django.http import *
from django .contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import View
from .forms import Customer_Profile
from django.db.models import Q

# Create your views here.


def home(request):
    elec = Product.objects.filter(category='M')
    sports = Product.objects.filter(category='TW')
    womens = Product.objects.filter(category='BM')

    return render(request, 'pages/home.html',context={"elec": elec, "sports": sports, "womens": womens})


# RECENTLY SERARCHED #######################################

def recent_search(request):
    elec = Product.objects.filter(category='M')
    sports = Product.objects.filter(category='TW')
    womens = Product.objects.filter(category='BM')

    return render(request, 'pages/recently.html', context={"elec": elec, "sports": sports, "womens": womens})


# USER ADDRESS SYSTEM #######################################

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Customer_Profile(request.POST)
            if form.is_valid():
                usr = request.user
                name = form.cleaned_data['name']
                mob = form.cleaned_data['mob']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipcode = form.cleaned_data['zipcode']
                reg = Customer(user=usr, name=name, mob=mob, city=city, state=state, zipcode=zipcode)
                messages.success(request, "Address updated successfully ✔")
                reg.save()
                return redirect('profile')
        else:
            form = Customer_Profile()
        return render(request, 'pages/customer_profile.html', {"form": form})
    else:
        return redirect('login')

# Sign page#####################################


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, 'User Already Exists !')
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, 'Email Already Exists !')
            return redirect('signup')

        if len(username) > 10 or len(username) == 0:
            messages.warning(request, 'Please Enter Valid Username!')
            return redirect('signup')

        if not len(password1) > 6:
            messages.error(request, 'password is too short! max.6 char')
            return redirect('signup')

        if password1 != password2:
            messages.error(request, " Entered Password does'nt matched ! 😷")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname

        myuser.save()
        messages.success(request, "your account has created successfully..✔")
        return redirect('login')

    return render(request, 'pages/signup.html')

# LOGOUT######################################################


def user_logout(request):
    logout(request)
    return redirect("home")

# PASSWORD DONE #####################################################


def done_pass(request):
    return render(request, 'pages/donepass.html')

# ADDRESS PAGE ######################################################


def address_page(request):
    address = Customer.objects.filter(user=request.user)
    print(address)
    return render(request, 'pages/address.html', {"address": address})

# CART########################################################


def user_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('/showcart')
    else:
        return redirect('login')

# SHOWING CART ########################################################


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_charge = 70.00
        total_amount = 0.0
        cart_product = [data for data in Cart.objects.all()if data.user == user]
        if cart_product:
            for data in cart_product:
                hold_amount = (data.quantity * data.product.discounted_price)
                amount += hold_amount
                totalamount = amount+shipping_charge
            print(user, cart_product)
            return render(request, 'pages/cart.html', {'cart': cart, 'totalamount': totalamount, 'amount': amount, 'shipping_charge': shipping_charge})
        else:
            return render(request, 'pages/nocart.html')
    else:
        return redirect('login')

# NO CART ########################################################


def no_cart(request):
    return render(request, 'pages/nocart.html')

# USERS ORDRDER######################################################


def my_order(request):
    placed_order = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'pages/order.html', {"placed_order": placed_order})

# PLUS CART ##########################################################


def plus_cart(request):
    if request.method == "GET":
        product_id = request.GET["product_id"]

        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
    
        c.quantity = c.quantity+1
        c.save()
        amount = 0.0
        shipping_charge = 70.00
        cart_product = [data for data in Cart.objects.all()if data.user == request.user]
        for data in cart_product:
            hold_amount = (data.quantity * data.product.discounted_price)
            amount += hold_amount
            totalamount = amount+shipping_charge
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
    return JsonResponse(data)


# MINUS CART ##########################################################

def minus_cart(request):
    if request.method == "GET":
        product_id = request.GET["product_id"]
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))

        c.quantity = c.quantity-1
        c.save()
        amount = 0.0
        shipping_charge = 70.00
        cart_product = [data for data in Cart.objects.all() if data.user == request.user]
        for data in cart_product:
            hold_amount = (data.quantity * data.product.discounted_price)
            amount += hold_amount
            totalamount = amount+shipping_charge
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
    return JsonResponse(data)

# REMOVE CART ##########################################################


def check_out(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_charge = 70.0
    totalamount = 0.0
    cart_product = [data for data in Cart.objects.all()if data.user == request.user]
    for data in cart_product:
        hold_amount = (data.quantity * data.product.discounted_price)
        amount += hold_amount
    totalamount = amount+shipping_charge
    return render(request, 'pages/checkout1.html', context={'add': add, 'totalamount': totalamount, 'cart_item': cart_items})


# PAYMENT ##########################################################

def payment_done(request):
    user = request.user
    cus_id = request.GET.get('cus-id')
    customer = Customer.objects.get(id=cus_id)
    cart = Cart.objects.filter(user=user)
    for cart_item in cart:
        OrderPlaced(user=user, customer=customer,product=cart_item.product, quantity=cart_item.quantity).save()
        cart_item.delete()
    return redirect('order')


# REMOVE CART ##########################################################

def remove_cart(request):
    if request.method == "GET":
        product_id = request.GET["product_id"]
    
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))

        c.delete()
        amount = 0.0
        shipping_charge = 70.00
        cart_product = [data for data in Cart.objects.all()
                        if data.user == request.user]
        for data in cart_product:
            hold_amount = (data.quantity * data.product.discounted_price)
            amount += hold_amount
            totalamount = amount+shipping_charge
        data = {
            # 'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
    return JsonResponse(data)


# PRODUCT DETAIL ######################################################

def product_detail(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        elec = Product.objects.filter(category='M')
        sports = Product.objects.filter(category='TW')
        womens = Product.objects.filter(category='BM')
        return render(request, 'pages/product-detail.html', context={"product": product, 'elec': elec, 'sports': sports, 'womens': womens})
    else:
        return redirect('info')

# INFO PAGE######################################################


def info(request):
    return render(request, 'pages/info.html')


# MOBILE FILTER ######################################################

def mobile(request, item=None):
    if item == None:
        mobiles = Product.objects.filter(category='M')

    elif item == 'redmi' or item == 'realme' or item == 'samsung' or item == 'Iphone':
        mobiles = Product.objects.filter(category='M').filter(brand=item)

    elif item == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=20000)
        print(item)

    elif item == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=20000)
        print(item)

    return render(request, 'pages/mobile.html', {'mobiles': mobiles})
