from django.urls import path 
# from links.views import home
from .import views
urlpatterns = [
    path("",views.home,name="home"),
    path('newlink/', views.NewLinkView.as_view(), name="newlink"),
    path('detail/<int:pk>', views.LinkDetailView.as_view(), name="detail"),
    
]
