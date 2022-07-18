from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class meta:
        model = Book
        fields = "__all__"