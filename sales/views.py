from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer
from django.views.generic.detail import DetailView
from django.utils import timezone


class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    paginate_by = 10

class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get('name')
        return Customer.objects.filter(first_name=name)  

class CustomerDetailView(DetailView):
    model = Customer    
    template_name = "sales/detail.html"

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj