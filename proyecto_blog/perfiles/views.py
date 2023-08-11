from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, authenticate

from perfiles.forms import UserRegisterForm
from perfiles.models import User

def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )


class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'


def mi_perfil(request):
    usuario = request.user
    data = {
        'form': UserRegisterForm(instance=usuario)
    }
    
    if request.method == 'POST':
        formulario = UserRegisterForm(data=request.POST, instance=usuario)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/")
        else:
            data["form"] = formulario
    
    return render(request, 'perfiles/mi-perfil.html', data)

#class EditarUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#    model = User
#    form_class = UserRegisterForm
#    template_name = 'perfiles/mi-perfil.html'
#    success_url = reverse('mi-perfil')

#    def form_valid(self, form):
#        form.instance.autor = self.request.user
#        return super().form_valid(form)

#    def test_func(self):
#        user = self.get_object()
#        return self.request.user == articulo.username