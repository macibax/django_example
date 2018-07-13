from django.conf.urls import url
from empleado import views

app_name = 'empleado'

urlpatterns = [
    #url('user_logout',views.user_logout,name='user_logout'),
    url('user_login',views.user_login,name='user_login'),
    url('reg_user',views.reg_user,name='reg_user'),
    url('reg_empleados',views.reg_empleados,name='reg_empleados'),
    url('reg_puestos',views.reg_puestos,name='reg_puestos'),
    url('index',views.index,name='index'),
    url('empleados',views.empleados,name='empleados'),
    url('puestos',views.puestos,name='puestos'),

]
