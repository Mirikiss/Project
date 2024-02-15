from django.urls import path
from . import views
from .views import withyou

app_name = 'blog'

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes', views.DelLike.as_view(), name='del_likes'),
    path('with_you/', withyou, name='with_you')]
