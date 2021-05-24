from re import template
from django.urls import path
from .views import UserEventListView, JoinEventView, PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView
from . import views 

urlpatterns = [
    path('', PostListView.as_view(), name='event-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='event-about'),
    path('events/<str:username>/', UserEventListView.as_view(), name='user-events'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('join/', JoinEventView.as_view(template_name = 'event/join_form.html'), name='join-event')
]