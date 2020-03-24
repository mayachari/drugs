"""SMILE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from drugs.views import content_upload, display_mols, drug_upload, display_drugs

urlpatterns = [
    path('admin/', admin.site.urls),
	path('upload-csv/', content_upload, name="content_upload"),
	path('upload-csv-drug/', drug_upload, name="drug_upload"),
	path('', display_mols, name='display_mols'),
	path('drugs/', display_drugs, name='display_drugs')
]
