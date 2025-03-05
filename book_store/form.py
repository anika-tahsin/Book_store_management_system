from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", 'description','published_year']
        widgets = {
            "title" : forms.TextInput(
                attrs= {
                    "class": "w-full p-2 border border-cyan-400 rounded-lg focus:outline-blue focus:ring-2 focus:ring-blue-400",
                    "placeholder": "Book Title",
                }
            ),
            "author" : forms.TextInput(
                attrs= {
                    "class": "w-full p-2 border border-cyan-400 rounded-lg focus:outline-blue focus:ring-2 focus:ring-blue-400",
                    "placeholder": "Book Author Name",
                }
            ),
            "description" : forms.Textarea(
                attrs={
                    "class": "w-full p-2 border border-cyan-400 rounded-lg focus:outline-blue focus:ring-2 focus:ring-blue-400",
                    "placeholder": "Description of the book",
                    "rows": 5,
                }
            ),
            "published_year" : forms.TextInput(
                attrs= {
                    "class": "w-full p-2 border border-cyan-400 rounded-lg focus:outline-blue focus:ring-2 focus:ring-blue-400",
                    "placeholder": "Publishing Year of the book",
                }
            ),
        }
