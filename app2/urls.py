from django.urls import path
from . import views

urlpatterns = [
    path("",views.hq,name='HQ'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('addcategory/', views.addcategory, name='addcat'),
    path('addcategory/addcatname/', views.addcatname, name='addcatname'),
    path('addproduct/', views.addproduct, name='addprod'),
    path('addproduct/addprodname/', views.addprodname, name='addprodname'),
]
