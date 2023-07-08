from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book
import requests


def get_book_data(query):
    if len(query) in [10, 13]:  # If it's an ISBN
        response = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q=isbn:{query}")
    else:  # If it's a book title
        response = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q=intitle:{query}")

    data = response.json()

    if response.status_code != 200 or "items" not in data:
        return None

    books_data = []
    for item in data["items"]:
        book_data = item["volumeInfo"]
        books_data.append({
            "title": book_data.get("title", ""),
            "author": ", ".join(book_data.get("authors", [])),
            "pub_date": book_data.get("publishedDate", ""),
            "isbn": book_data.get("industryIdentifiers", [{"identifier": None}])[0]["identifier"],
            "thumbnail": book_data.get("imageLinks", {}).get("thumbnail", "")
        })

    return books_data


def index(request):
    all_books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html', {'all_books': all_books})


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')

        books_data = get_book_data(query)
        if books_data:
            # Save book data into session
            request.session['books_data'] = books_data
            return render(request, 'books/search_results.html', {'books': books_data})
        else:
            messages.warning(request, 'Book not found or invalid query')
    return render(request, 'books/index.html', {'all_books': Book.objects.filter(user=request.user)})


def confirm_add(request, isbn):
    if 'books_data' not in request.session:
        return redirect('books:index')

    books_data = request.session['books_data']
    book_data = next(
        (book for book in books_data if book["isbn"] == isbn), None)

    if book_data is None:
        messages.error(request, 'Book not found')
        return redirect('books:index')

    if request.method == 'POST':
        if Book.objects.filter(isbn=isbn, user=request.user).exists():
            messages.warning(
                request, 'You already have this book in your library')
        else:
            new_book = Book(user=request.user, **book_data)
            new_book.save()
            messages.success(request, 'Book added successfully')
        return redirect('books:index')

    return render(request, 'books/confirm_add.html', {'book': book_data})


def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully')
    return redirect('books:index')
