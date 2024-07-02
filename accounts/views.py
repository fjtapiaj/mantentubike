from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


def accounts(request):
    # Tu lógica para la vista de accounts
    return render(request, 'accounts/login.html')

def password_reset_form (request):
    return render(request, 'accounts/password_reset_form.html')


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('ruta_de_exito')  # Reemplaza 'ruta_de_exito' con la URL a la que deseas redirigir tras el login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('conometro/cronometro.html')  # Reemplaza 'ruta_de_exito' con la URL a la que deseas redirigir tras el login
            else:
                # Mensaje de error si el usuario no está autenticado
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Usuario o contraseña incorrectos.'})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('ruta_de_exito')  # Reemplaza 'ruta_de_exito' con la URL a la que deseas redirigir tras el logout
    return render(request, 'accounts/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Crea el perfil del usuario si es necesario
            # Ejemplo: Profile.objects.create(user=user, ...)
            return redirect('bienvenida')  # Reemplaza 'ruta_de_exito' con la URL a la que deseas redirigir tras el registro
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


