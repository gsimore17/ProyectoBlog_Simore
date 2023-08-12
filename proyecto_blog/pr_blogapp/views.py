from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pr_blogapp.models import Articulo
from pr_blogapp.forms import ArticuloForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class ListaArticulosView(ListView):
    model = Articulo
    template_name = 'pr_blogapp/lista_articulos.html'
    context_object_name = 'articulos'
    ordering = ['-fecha']


class DetalleArticuloView(DetailView): #LoginRequiredMixin,
    model = Articulo
    template_name = 'pr_blogapp/detalle_articulo.html'
    context_object_name = 'articulo'


class CrearArticuloView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'pr_blogapp/crear_articulo.html'
    success_url = 'lista_articulos'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarArticuloView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'pr_blogapp/editar_articulo.html'
    success_url = reverse_lazy ('lista_articulos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor

class BorrarArticuloView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'pr_blogapp/borrar_articulo.html'
    success_url = reverse_lazy ('lista_articulos')

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor