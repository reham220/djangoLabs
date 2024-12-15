from django.shortcuts import render
from .models import Book  
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Count
from django.shortcuts import redirect
from .forms import BookForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address
from .forms import StudentForm, AddressForm



#def index(request):
 #name = request.GET.get("name") or "world!"
# return render(request, "bookmodule/index.html") 

#def index2(request, val1 = 0): #add the view function (index2)
 #return HttpResponse("value1 = "+str(val1))


#def index(request):
 #name = request.GET.get("name") or "world!"
 #return render(request, "bookmodule/index.html" , {"name": name}) #your render line

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def links_page(request):
    return render(request, 'bookmodule/links.html')
def formatting(request):
    return render(request, 'bookmodule/formatting.html')
def listing(request):
    return render(request, "bookmodule/listing.html")
def tables(request):
    return render(request, 'bookmodule/tables.html')
def search(request):
   if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
 # now filter
    books = __getBooksList()
    newBooks = []
    for item in books:
        contained = False
        if isTitle and string in item['title'].lower(): contained = True
        if not contained and isAuthor and string in item['author'].lower():contained = True

        if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList.html', {'books':newBooks})

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]
def search_results(request):
    books = request.session.pop('filtered_books', [])  # Get and clear the session data
    return render(request, 'bookmodule/bookList.html', {'books': books})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull =False).filter(title__icontains='Delivery')[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
#def add_book(request):
#    return render(request, 'bookmodule/add_book.html')


#Only call this function once!
def __insertion_db():
    book1 = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 2)
    book1.save()
    book2 = Book(title = 'Reversing: Secrets of Reverse Engineering', author = 'E. Eilam', edition = 4)
    book2.save()
    book3 = Book(title = 'The Hundred-Page Machine Learning Book', author = 'Andriy Burkov', edition = 3)
    book3.save()



def task1_view(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})


def task2_view(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})


def task3_view(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')) )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})


def task5_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})


def city_count_view(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'studentmodule/city_count.html', {'city_stats': city_stats})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})



def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')
    return render(request, 'bookmodule/add_book.html')

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/edit_book.html', {'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')



def add_book_form(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book_form.html', {'form': form})


def edit_book_form(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_book_form.html', {'form': form})






def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'delete_student.html', {'student': student})



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def list_images(request):
    images = ImageModel.objects.all()
    return render(request, 'list_images.html', {'images': images})


