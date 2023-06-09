from django.shortcuts import render,redirect 
from .models import Product, Article #import Product from models
from django.core.paginator import Paginator
from .forms import NewUserForm
from django.contrib.auth import login  #add this
from django.contrib import messages #import messages
from django.contrib.auth import login,logout, authenticate #import authenticate
from django.contrib.auth.forms import AuthenticationForm #import AuthenticationForm
from .models import BlogPost





# Create your views here.
def homepage(request):	
	product = Product.objects.all()[:4]
	return render(request=request, template_name="main/home.html", context={'product': product})

def products(request):
	products = Product.objects.all()
	paginator = Paginator(products, 18)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	messages.info(request, "Welcome to the products page")#Add messages like
	return render(request = request, template_name="main/products.html", context = {"page_obj":page_obj})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have logged out successfully Bro.")
    return redirect("main:homepage")
    
def blog(request):
	blog = Article.objects.all().order_by('-article_published')
	paginator = Paginator(blog, 25)
	page_number = request.GET.get('page')
	blog_obj = paginator.get_page(page_number)
	return render(request=request, template_name="main/blog.html", context={"blog":blog_obj})    
    
def article(request, article_page):
    article = Article.objects.get(article_slug=article_page)
    return render(request=request, template_name='main/article.html', context={"article": article})    
    
    