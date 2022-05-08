


from django.urls import path
from . import views##aşağıdaki path için
urlpatterns = [
    path("",views.index, name="index"),
    path("index",views.index),
    path("/",views.index),
    path("spams/",views.spams),
    path("regular/",views.regular),

]
