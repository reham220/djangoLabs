from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Book

# Create your views here.
def home(request):
    return render(request,'mybook/home.html')

def book_list(request):
    books=Book.objects.all()
    print(books)
    return render(request,'mybook/book_list.html',{'books':books})


# object = get_object_or_404(ModelName, lookup_field=value)

def book_details(request,bID):
    book=get_object_or_404(Book,pk=bID)
    return render(request,'mybook/book_detail.html', {'book': book})

def index(request,name):
    return render(request,'mybook/index.html',{'name':name})
    # return HttpResponse("Welcome to our library "+name+" !")
