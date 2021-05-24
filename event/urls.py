from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView
from . import views 

urlpatterns = [
    path('', PostListView.as_view(), name='event-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='event-about'),
    path('events/', views.events, name='events'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('join/', views.joinEvent, name='join-event')
]