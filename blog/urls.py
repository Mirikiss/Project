from django.urls import path
from django.urls import include

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog'))
]
