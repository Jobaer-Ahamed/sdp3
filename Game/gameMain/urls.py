from django.urls import path
from .import views

app_name = "gameMain"
urlpatterns = [
   path("",views.index,name="Index"),
   path("gameMain/<int:id>/<str:name>/",views.gameroom,name="Gameroom")

]