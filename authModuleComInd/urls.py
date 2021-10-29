"""authModuleComInd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authAppComInd import views  as authAppViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productGet/', authAppViews.ProductoCreateView.as_view()),
    path('productList/', authAppViews.ProductoListView.as_view()),
    path('productActualizar/<int:pk>/', authAppViews.ProductoUpdateView.as_view()),
    path('productBorrar/<int:pk>/', authAppViews.ProductoDeleteView.as_view()),
    path('comunidades/', authAppViews.ComunidadCreateView.as_view()),
    path('comunidadesList/', authAppViews.ComunidadListView.as_view()),
    path('comunidadesActualizar/<int:pk>/', authAppViews.ComunidadUpdateView.as_view()),
    path('comunidadesBorrar/<int:pk>/', authAppViews.ComunidadDeleteView.as_view()),
    path('comunidadesYproductos/', authAppViews.Produc_comunCreateView.as_view()),
    path('comunidadesYproductosList/', authAppViews.Produc_comunListView.as_view())
    
    
]
