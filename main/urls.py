"""
URL configuration for sku project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *


urlpatterns = [
    path('', home, name='home'),

    path('view_sku/', View__SKU, name='view_sku'),
    path('add_sku/', Change__SKU, name='add_sku'),
    path('change_sku/<int:pid>/', Change__SKU, name='change_sku'),
    path('delete_sku/<int:pid>/', Delete__SKU, name='delete_sku'),
    # path('import_sku/', Import__SKU, name='import_sku'),


    path('view_brand/', View__Brand, name='view_brand'),
    path('add_brand/', Change__Brand, name='add_brand'),
    path('change_brand/<int:id>/', Change__Brand, name='change_brand'),
    path('delete_brand/<int:id>/', Delete__Brand, name='delete_brand'),

    path('view_article_type/', View__Article__Type, name='view_article_type'),
    path('add_article_type/', Change__Article__Type, name='add_article_type'),
    path('change_article_type/<int:id>/', Change__Article__Type, name='change_article_type'),
    path('delete_article_type/<int:id>/', Delete__Article__Type, name='delete_article_type'),

    path('view_gender/', View__Gender, name='view_gender'),
    path('add_gender/', Change__Gender, name='add_gender'),
    path('change_gender/<int:id>/', Change__Gender, name='change_gender'),
    path('delete_gender/<int:id>/', Delete__Gender, name='delete_gender'),

    path('view_size/', View__Size, name='view_size'),
    path('add_size/', Change__Size, name='add_size'),
    path('change_size/<int:id>/', Change__Size, name='change_size'),
    path('delete_size/<int:id>/', Delete__Size, name='delete_size'),

    path('view_color/', View__Color, name='view_color'),
    path('add_color/', Change__Color, name='add_color'),
    path('change_color/<int:id>/', Change__Color, name='change_color'),
    path('delete_color/<int:id>/', Delete__Color, name='delete_color'),

    path('view_uom', View__UOM, name='view_uom'),
    path('add_uom/', Change__UOM, name='add_uom'),
    path('change_uom/<int:id>/', Change__UOM, name='change_uom'),
    path('delete_uom/<int:id>/', Delete__UOM, name='delete_uom'),
    path('copy-sku/<int:pid>/', Copy__SKU, name='copy_sku'),

    path('meesho/', Meesho_Template, name='meesho'),
    path('flipkart/', Flipkart_Template, name='flipkart'),
    path('snapdeal/', Snapdeal_Template, name='snapdeal'),
    path('myntra/', Myntra_Template, name='myntra'),

    path('save_video/', save_video, name='save_video'),
    path('record/', record_video_page, name='record_video'),
    path('view_vms/', View__VMS, name='view_vms'),

    path('print_sku/<int:pid>/', Print__SKU, name='print_sku'),
    path('print_barcode/<int:pid>/', Print__Barcode, name='print_barcode'),
]
