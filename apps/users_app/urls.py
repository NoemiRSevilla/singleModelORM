from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.addBook),
    url(r'^books/(?P<id>\d+)$', views.bookInfo),
    url(r'^authors$', views.addAuthor),
    url(r'^authors/(?P<id>\d+)$', views.authorInfo),
    url(r'^books/(?P<id>\d+)/add$', views.add_author_to_book),
    url(r'^authors/(?P<id>\d+)/add$', views.add_book_to_author)
]