from django.urls import path
from . import views
# Create Your urls here:


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail_view'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),

    # path('', views.post_list, name='posts_list'),
    # path('<int:pk>/', views.detail_view, name='post_detail_view'),
    # path('create/', views.create_post_view, name='create_post'),
    # path('<int:pk>/update/', views.update_post_view, name='update_post'),
    # path('<int:pk>/delete/', views.delete_post_view, name='delete_post'),
]
