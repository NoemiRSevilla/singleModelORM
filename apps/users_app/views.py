from django.shortcuts import render, redirect
from .models import Books, Authors


def addBook(request):
    if request.method == "GET":
        context = {
            "allBooks": Books.objects.all()
        }
        return render(request, "addBook.html", context)
    if request.method == "POST":
        newBook = Books.objects.create
        newBook(title=request.POST['title'],
                description=request.POST['description'])
        return redirect("/")


def addAuthor(request):
    if request.method == "GET":
        context = {
            "allAuthors": Authors.objects.all(),
        }
        return render(request, "addAuthor.html", context)
    if request.method == "POST":
        newAuthor = Authors.objects.create
        newAuthor(first_name=request.POST['first_name'],
                  last_name=request.POST['last_name'], notes=request.POST['notes'])
        return redirect("/authors")


def bookInfo(request, id):
    if request.method == "GET":
        context = {
            "showBook": Books.objects.get(id=id),
            "authorsBook": Books.objects.get(id=id).authors.all(),
            "allAuthors": Authors.objects.all(),
        }
        return render(request, "bookInfo.html", context)
    if request.method == "POST":
        return redirect(f"/book/{id}")

def add_author_to_book(request, id):
    if request.method == "GET":
        context = {
            "showBook": Books.objects.get(id=id),
            "authorsBook": Books.objects.get(id=id).authors.all(),
            "allAuthors": Authors.objects.all(),
            "authorsinfo": Authors.objects.get
        }
        return render(request, "bookInfo.html", context)
    if request.method == "POST":
        Books.objects.get(id=id).authors.add(Authors.objects.get(id=request.POST['author_id']))
        return redirect(f"/books/{id}")

def add_book_to_author(request, id):
    if request.method == "GET":
        context = {
            "showAuthor": Authors.objects.get(id=id),
            "authorsofbook": Authors.objects.get(id=id).books.all(),
            "allAuthors": Authors.objects.all(),
            "booksinfo": Books.objects.get
        }
        return render(request, "authorInfo.html", context)
    if request.method == "POST":
        Authors.objects.get(id=id).books.add(Books.objects.get(id=request.POST['book_id']))
        return redirect(f"/authors/{id}")

def authorInfo(request, id):
    if request.method == "GET":
        context = {
            "showAuthor": Authors.objects.get(id=id),
            "allBooks": Books.objects.all(),
            "booksbyauthor": Authors.objects.get(id=id).books.all(),
        }

        return render(request, "authorInfo.html", context)
    if request.method == "POST":
        value=request.POST['value']
        book=Books.objects.get(id=value)
        showAuthor.books.add(book)
        return redirect(f"/author/{id}")