from django.urls import path
from .views import proxy_image

urlpatterns = [
    path('<path:image_url>/', proxy_image, name='proxy_image'),
]