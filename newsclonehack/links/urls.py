from django.urls import path 
# from links.views import home
from .import views
urlpatterns = [
    path("",views.home,name="home"),
    path('newlink/', views.NewLinkView.as_view(), name="newlink"),
    path('detail/<int:pk>', views.LinkDetailView.as_view(), name="detail"),
    #path('lists/<str:username>', views.LinkListView.as_view(), name="lists"),
    path('lists/<str:username>/<int:id>', views.LinkListView.as_view(), name="lists"),
    
    
]




