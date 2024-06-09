from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for obj in context_data['object_list']:
            current_version = Version.objects.filter(product_id=obj.pk, is_current=True).first()
            obj.version = current_version
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"name: {name}, email: {phone}, message: {message}")
        return self.get(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login"

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/users/login"

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        print(self.request.user)
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)