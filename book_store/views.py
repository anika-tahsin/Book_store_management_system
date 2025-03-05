from django.shortcuts import render, redirect
from .models import Book
from .form import BookForm

# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all().order_by("-updated_at"),
    }
    return render(request,'index.html',context)


def add(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm()

    context = {
        "form": book_form,
    }

    return render(request, 'book_form.html', context)
        

def edit(request, id):
    clicked_blog = Book.objects.get(id=id)

    if request.method == 'POST':
        book_form = BookForm(request.POST, instance=clicked_blog)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm(instance=clicked_blog)

    context = {
        "form": book_form,
    }

    return render(request, 'book_form.html', context)

def delete(request,id):
    clicked_blog = Book.objects.get(id=id)
    clicked_blog.delete()
    return redirect("book_list")