from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('books/', list_books, name='list_books'),
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
#     path('register/', views.register, name='register'),
# ]

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),  
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'), 
]