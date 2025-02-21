from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .models import *
from django.contrib import messages

def home(request):
    total_readers = Reader.objects.count()
    total_books = Book.objects.count()
    return render(request, 'libraryApp/home.html', {'total_readers': total_readers, 'total_books': total_books})

def readers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        if name and email and mobile:
            Reader.objects.create(name=name, email=email, mobile=mobile)
            messages.success(request, "Reader added successfully!")
        else:
            messages.error(request, "All fields are required!")

    all_readers = Reader.objects.all()
    return render(request, 'libraryApp/readers.html', {'readers': all_readers})

def edit_reader(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)

    if request.method == 'POST':
        reader.name = request.POST.get('name')
        reader.email = request.POST.get('email')
        reader.mobile = request.POST.get('mobile')
        reader.save()
        messages.success(request, "Reader updated successfully!")
        return redirect('readers')

    return render(request, 'libraryApp/readers.html', {'reader': reader})

def books(request):
    all_books = Book.objects.all()
    return render(request, 'libraryApp/books.html', {'books': all_books})

def add_to_bag(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    readers = Reader.objects.all()  # Fetch all readers for selection

    if request.method == 'POST':
        reader_id = request.POST.get('reader')
        quantity = int(request.POST.get('quantity', 1))

        if not reader_id:
            messages.error(request, "Please select a reader!")
            return redirect('books')

        reader = Reader.objects.get(id=reader_id)

        if book.quantity >= quantity:
            BorrowedBook.objects.create(reader=reader, book=book, quantity=quantity)
            book.quantity -= quantity
            book.save()
            messages.success(request, "Book added to bag successfully!")
        else:
            messages.error(request, "Not enough stock available!")

        return redirect('books')

    return render(request, 'libraryApp/add_to_bag.html', {'book': book, 'readers': readers})

def bag(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'libraryApp/bag.html', {'borrowed_books': borrowed_books})

def return_book_page(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'libraryApp/return_book.html', {'borrowed_books': borrowed_books})

def return_book(request, borrow_id):
    borrowed = get_object_or_404(BorrowedBook, id=borrow_id)

    # Restore book quantity
    borrowed.book.quantity += borrowed.quantity
    borrowed.book.save()

    # Delete borrowed record
    borrowed.delete()
    
    messages.success(request, "Book returned successfully!")
    return redirect('return_book_page')