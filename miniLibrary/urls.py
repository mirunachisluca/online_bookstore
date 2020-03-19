from django.http import HttpResponseRedirect
from django.views import generic
from django.conf import settings 
from django.conf.urls.static import static

from django.urls import path, include

from miniLibrary.views import BookDetail, UserCreate, LoginView, UserDetail,BookCreate, BookUpdate, BookDelete, CartView, OrderView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # books urls
    path('books/', views.books, name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'), # ex: /miniLibrary/books/5/
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('books/user/registration/', UserCreate.as_view(), name='user-register'),
    path("books/add/", BookCreate.as_view(), name='book-add'),
    path("books/<int:pk>/update/", BookUpdate.as_view(), name='book-update'),
    path("books/<int:pk>/delete/", BookDelete.as_view(), name='book-delete'),
    path('books/<int:book_id>/upload/', views.upload_file, name='image-upload'),
    path('books/login/',LoginView.as_view(), name = 'login-view' ),
    path('books/<int:book_id>/add/',views.addToCart, name = 'login-view' ),
    path('books/cart/',CartView.as_view(), name = 'cart-view' ),
    path('books/order/',OrderView.as_view(), name = 'order-view' ),
    path('books/logout',views.logout, name='logout'),

    # courses urls
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.courseDetail, name='course-detail'),
]
