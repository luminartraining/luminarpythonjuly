from django.forms import  ModelForm


from .models import  Book


class BookCreateFrm(ModelForm):

    class Meta:
        model=Book
        fields='__all__'