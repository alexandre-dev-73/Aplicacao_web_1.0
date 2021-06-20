from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


def register(request):
    """Faz o cadastro de um novo usuario."""
    if request.method != 'POST':
        #Exibe o formulario preenchido
        form = UserCreationForm()
    else:
        #Processa o formulario preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Faz login do usuário eo redireciona para a pagina inicial
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            auth_views.LoginView.as_view(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)