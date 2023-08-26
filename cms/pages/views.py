


from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from . models import Pages, CategoryPage
from . forms import ProductForm



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'account/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('showProducts')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'account/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def ShowAllProducts(request):
    
    category = request.GET.get('category')

    if category == None:
        products = Pages.objects.order_by('-createionDate').filter(published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 2)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)             
    else:
        products = Pages.objects.filter(category__name=category)
       
    
    categories = CategoryPage.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'pages/showProducts.html', context)



@login_required(login_url='showProducts')
def productDetail(request, pk):
    eachProduct = Pages.objects.get(id=pk)
    context = {
        'eachProduct': eachProduct,
    }

    return render(request, 'pages/productDetail.html', context)



@login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'pages/addProduct.html', context)


@login_required(login_url='showProducts')
def updateProduct(request,pk):
    product = Pages.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        "form":form
    }

    return render(request, 'pages/updateProduct.html', context)



@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Pages.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')



@login_required(login_url='showProducts')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Pages.objects.filter(title__icontains=query) 
            return render(request, 'pages/searchbar.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'pages/searchbar.html', {})


