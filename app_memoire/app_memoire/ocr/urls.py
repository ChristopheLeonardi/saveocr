from django.urls import path
from .views import image_request, results
from . import views
from django.conf.urls.static import static

urlpatterns = [
    #path('form/', ocr_form, name='ocr-form'),
    path('form/', views.image_request, name = "image-request"),
    path('results/', views.results, name = "results")
    
]     

