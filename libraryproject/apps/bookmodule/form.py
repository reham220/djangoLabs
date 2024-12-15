from django import forms
from .models import Book
from .models import Student, Address

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'student']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age']

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['street', 'city', 'students']


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image']

