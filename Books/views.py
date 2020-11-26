from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView,TemplateView
from django.urls import reverse_lazy
from Books.models import Book
from .forms import BookCreateFrm

class BookList(TemplateView):
    template_name = "Books/book_list1.html"
    model=Book
    context={}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context["books"]=self.querySet()
        return render(request,self.template_name,self.context)


class BookCreate(CreateView):
    model = Book
    form_class = BookCreateFrm()
    template_name = "Books/book_form.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class
        return  render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=BookCreateFrm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")




class BookEdit(TemplateView):
    model = Book
    form_class=BookCreateFrm()

    template_name = "Books/editbook.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.getQuery(id)
        form=BookCreateFrm(instance=qs)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def getQuery(self,id):
        return self.model.objects.get(id=id)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.getQuery(id)
        form=BookCreateFrm(instance=qs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        else:
            return render(request, self.template_name, self.context)



class BookView(TemplateView):
    model = Book
    template_name = "Books/book_detail.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.model.objects.get(id=id)
        self.context["book"]=qs
        return render(request,self.template_name,self.context)


class BookDelete(DeleteView):
    model = Book
    template_name = "Books/book_confirm_delete.html"
    form_class=BookCreateFrm()
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.model.objects.get(id=id)
        self.context["form"]=BookCreateFrm(instance=qs)
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect("book_list")







# //mainproject

# //rest


