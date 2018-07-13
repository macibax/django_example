from django.shortcuts import render
from empleado.forms import RegEmpleado, RegPuesto, UserProfileInfoForm, UserForm
from empleado.models import Empleado, Puesto, UserProfileInfo

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context_data = {}
    return render(request,'empleado/index.html',context_data)

@login_required #DECORADOR QUE REQUIERE QUE ESTE LOGEADO PARA USARSE
def user_logout(request):
    #LOGEA AL USUARIO
    logout(request)
    return index(request)

def user_login(request):
    context_data = {}
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('pass')

        #VERIFICA AL USUARIO AUTOMATICAMENTE:
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                #LOGS EL USUARIO
                login(request,user)
                #REDIRECCIONA PAGINA
                #return HttpResponseRedirect(reverse('index'))
                return index(request)
            else:
                return HttpResponse("CUENTA NO ACTIVA")
        else:
            print("login fallado")
            print("usuario: {} y pass {}".format(username,password))
            return HttpResponse("login invalido")
    else:
        return render(request,'empleado/user_login.html',context_data)


def reg_user(request):

    registrado = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password) #hashes el passrod
            user.save() #se guardan los cambios del hashed pass

            profile = profile_form.save(commit=False) #el commit indica si quieres que se grabe en la base de datos
            profile.user = user #onetoone field

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registrado = True
        else:
            print(user_form.errors,profile_form.errors)
    context_data = {
        'user_form':UserForm(),
        'profile_form':UserProfileInfoForm(),
        'registrado': registrado,
    }
    return render(request,'empleado/reg_user.html',context_data)

def empleados(request):
    empleados_data = Empleado.objects.order_by('nombre')
    context_data = {'empleados_data':empleados_data}
    return render(request,'empleado/empleados.html',context_data)

def reg_empleados(request):
    context_data = {
    'form':RegEmpleado(),
    }

    if request.method == 'POST':
        form = RegEmpleado(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

    return render(request,'empleado/reg_empleados.html',context_data)

def puestos(request):
    puestos_data = Puesto.objects.order_by('nombre')
    context_data = {'puestos_data':puestos_data}
    return render(request,'empleado/puestos.html',context_data)

def reg_puestos(request):
    context_data = {
    'form':RegPuesto(),
    }

    if request.method == 'POST':
        form = RegPuesto(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

    return render(request,'empleado/reg_puestos.html',context_data)
