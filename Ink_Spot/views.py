from django.shortcuts import render , HttpResponse 

# Import packages from Models
from .models.product import Product
from .models.categories import Categories
from .models.book import Book
from .models.b_catogeries import B_categories



# Create your views here.
def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')




# for Books

book = Book.get_all()

def book(request):
    book = None
    bcat = B_categories.all_catogaries()
    categoryID = request.GET.get('categories')
    if categoryID:
        book = Book.get_all_filter(categoryID )
    else:
        book = Book.get_all()

    bdata = {} 
    bdata['book'] = book
    bdata['b_catogereis'] = bcat

    return render(request, 'book.html',bdata)

  # for product _ stationary items
def product(request):
    product = None
    cat = Categories.all_catogaries()
    categoryID = request.GET.get('categories')
    print(categoryID)
    
    if categoryID:
        product = Product.get_all_filter(categoryID) 
    else:
        product = Product.get_all() 


    data = {} 
    data['product'] = product
    data['catogereis'] = cat
    return render(request, 'product.html',data)

   
     