from django.urls import path
from . import views
# Create Your urls here:


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
