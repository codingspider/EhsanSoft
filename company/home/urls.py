from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    path('commerce/', views.commerce, name="commerce"),
    path('loyalty/', views.loyalty, name="loyalty"),
    path('marketing/', views.marketing, name="marketing"),
    path('crm/', views.crm, name="crm"),
    path('online/', views.online, name="online"),
    path('feedback/', views.feedback, name="feedback"),
    path('bookasoft/', views.bookasoft, name="bookasoft"),
    path('contact/', views.contact, name="contact"),
    path('partners/', views.partners, name="partners"),
    path('full/stack', views.admincrm)



]
