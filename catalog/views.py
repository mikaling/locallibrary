from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.

def index(request):
    '''View function for home page of site'''

    #  generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #  the 'all()' in implied by default
    num_authors = Author.objects.count()

    # number of genres
    num_genres = Genre.objects.count()

    # number of books with "dummy" in title (case-insensitive)
    num_dummy_books = Book.objects.filter(title__icontains='dummy').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_dummy_books': num_dummy_books,
    }

    #  render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
