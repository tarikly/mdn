from django.urls import path, re_path
from . import views

urlpatterns = [

        path('', views.index, name='index'),
        path('authors', views.AuthorListView.as_view(), name='authors'),
        path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
        path('books', views.BookListView.as_view(), name='books'),
        #path('books/<str:book_year>', views.BookFilterListView.as_view(), name='books-filter'),
        re_path(r'^books/(?P<pub_year>[1-2][0-9]{3})/$', views.BookFilterByYearListView.as_view(), name='books-filter'),
        re_path(r'^books/(?P<pub_year>[1-2][0-9]{3})/(?P<pub_month>0?[1-9]|1[012])$', views.BookFilterByYearMonthListView.as_view(), name='books-filter'),
        re_path(r'^books/(?P<pub_year>[1-2][0-9]{3})/(?P<pub_month>0?[1-9]|1[012])/(?P<pub_day>0?[1-9]|[12]\d|3[0-1])/$', views.BookFilterByYearMonthDayListView.as_view(), name='books-filter'),
        path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]
