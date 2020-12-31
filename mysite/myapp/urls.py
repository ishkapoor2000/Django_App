from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
]
