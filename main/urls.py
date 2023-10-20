from django.urls import path
import main.views as views

# para cargar imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # General views
    path('', views.index, name='index'),
    path('test1', views.test1, name='test1'),

] 