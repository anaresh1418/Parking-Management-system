from django.contrib import admin
from django.urls import path
from application1 import views

urlpatterns = [
    path('',views.loginfrom,name="loginpage"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard',views.dashboard,name="dashboard"),

    path('categorymodule',views.add_category1,name="addcategory"),
    path('categorysearch/',views.categorysearch,name='categorysearch'),
    path('categorymodule',views.categorymodule,name="categorymodule"),

    path('confirm_delete/<int:id>/', views.deletecategory, name='confirm_delete'),
    path('confirmed_delete/<int:id>/', views.confirmed_delete, name='confirmed_delete'),

    path('editcategory/<int:id>/',views.editcategory,name="edit"),
    path('updatecategory/<int:id>/',views.updatecategory,name="updatecategory"),
    path('active/<int:id>/',views.active_category,name='danger'),
    path('deactivate/<int:id>/',views.deactive_category,name='success'),

    path('vehicleentry',views.vehicleentry,name="vehicleentry"),
    path('leave/<int:id>/',views.parked_vehicle,name="leave"),
    path('park/<int:id>/',views.leaved_vehicle,name="park"),

    path('managevehicle',views.managevehicle,name="managevehicle"),
    path('vehiclesearch/',views.vehiclesearch,name='vehiclesearch'),
    path('managevehiclesearch/',views.managevehicesearch,name='managevehiclesearch'),
    path('parkingsearch/',views.parkingsearch,name='parkingsearch'),
    path('status_manage_vehicle/<int:id>/',views.status_manage_vehicle,name="status_manage_vehicle"),
    path('parkingstatus',views.parkingstatus,name="parkingstatus"),
    path('reset',views.reset,name="reset"),
    path('changepassword',views.resetpassword,name='respsw'),
    path('reciept/<int:id>/',views.vehicle_reciept,name='reciept'),
]