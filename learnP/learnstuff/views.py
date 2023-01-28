from datetime import date 
from .models import Book_stem
from django.shortcuts import render

def get_post_date(post):
    return post["date"]

# Create your views here.
def index(request):
  Book = Book_stem.objects.all()
  context = {"book" : Book}
  return render(request, "learnstuff/index.html", context)
def all_post(request):
    pass

def book_detail(request, slug):
    book = Book_stem.objects.get(slug=slug)
    return render(request, "learnstuff/post-detail.html", {'book': book})

