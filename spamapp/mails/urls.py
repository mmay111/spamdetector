


from django.urls import path
from . import views##aşağıdaki path için
urlpatterns = [
    path("",views.index, name="mails"),
    path("index",views.index),
]
