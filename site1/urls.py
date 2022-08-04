from django.urls import path
from site1.views import *

urlpatterns = [
    path('' , index_view),
    path('about' , about_view),
    path('contact' ,contact_view )
]