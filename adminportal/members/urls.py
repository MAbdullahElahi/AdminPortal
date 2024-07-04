from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), 
    path('login', views.login_user), 
    path('addsale', views.addSale), 
    path('updatesale', views.updateSale), 
    path('deletesale', views.deleteSale),
    path('logout', views.logout_user)
]
