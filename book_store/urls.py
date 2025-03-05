from django.urls import path
from .import views

urlpatterns= [
    path("", views.index, name='book_list'),
    path("add/", views.add, name='book_add'),
    path("edit/<int:id>/", views.edit, name='book_edit'),
    path("delete/<int:id>/", views.delete, name='book_delete'),
]
