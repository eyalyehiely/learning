
from django.urls import path, include
from .views import *

urlpatterns = [
    path('lobby/',lobby_page, name="lobby page"),
    path('codeblock/<uuid:id>/',get_code_block,name="get code block")
]