from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import cadastro, login, logout, dashboard
from show.views import home, lista, listaevento,registronomelista,comprovante, adicionar_nome_lista_com_cadastro, adicionar_nome_lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('lista', lista, name='lista'),
    path('listaevento', listaevento, name='listaevento'),
    path('lista/<int:id>', lista, name='lista'),
    path('registronomelista', adicionar_nome_lista, name='adicionar_nome_lista'),
    path('adicionar_nome_lista_com_cadastro', adicionar_nome_lista_com_cadastro, name='adicionar_nome_lista_com_cadastro'),

    path('registronomelista/<int:id>', registronomelista, name='registronomelista'),
    path('comprovante', comprovante, name='comprovante'),
    path('comprovante/<int:id>', comprovante, name='comprovante'),
    path('dashboard', dashboard, name='dashboard'),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)