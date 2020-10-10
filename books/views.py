from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

zonars=["romance","horror","health","sci_fi"]
books={}
descriptions={}
books["romance"]=["love_and_life","romeo"]
books["horror"]=["love_and_life","romeo"]
books["health"]=["love_and_life","romeo"]
books["sci_fi"]=["love_and_life","romeo"]
descriptions["romance"]=["this is first book","thi is second book"]
books_requested=[]
# Create your views here.
def home(request):
    if request.method=="POST":
        names={}
        names["author"]=request.POST["author"]
        names["book_name"]=request.POST["book_name"]
        names["email"]=request.POST["email"]
        names["fullName"]=request.POST["fullName"]
        global books_requested
        if len(books_requested)==10:
            books_requested=[]

        books_requested.append(names)
        messages.success(request,"request for book sent successfully")
        return render(request,"books/home.html")
    return render(request,"books/home.html")

def explore(request):
    global zonars
    categories={"zonars":zonars}
    return render(request,"books/bookshelf.html",categories)
def books_display(request,zonar="zz"):
    ###########
    ###########
    zonar=zonar
    global books
    zonar_books={"books":books[zonar],"zonar":zonar}


    return render(request,"books/books.html",zonar_books)
def bookinfo(request,zonar,book_name):
    book={}
    book["title"]=book_name
    book["zonar"]=zonar
    book["description"]=descriptions[zonar][books[zonar].index(book_name)]

    return render(request,"books/bookinfo.html",{"book":book})
def book_requests(request):
    global books_requested

    return render(request,"books/book_requests.html",{"books":books_requested})
