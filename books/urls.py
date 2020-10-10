from django.urls import path
from . import views

urlpatterns=[
 path("",views.home,name="home"),
 path("explore/",views.explore,name="explore"),
 path("books/<zonar>/",views.books_display,name="books_display"),
 path("books/<zonar>/<book_name>/",views.bookinfo,name="bookinfo"),
 path("staines/",views.book_requests,name="book_requests"),
 ]
