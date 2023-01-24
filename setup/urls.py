from django.contrib import admin
from django.urls import path, include
from crud.views import login, home, salvar, editar, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('home.html', home),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]