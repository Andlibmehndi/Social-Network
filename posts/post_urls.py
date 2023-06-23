from django.urls import path
from .views import PostLikeToggle, PostCreateAndList, PostUpdateAndDelete

# Post Routes
urlpatterns = [
    path('', PostCreateAndList.as_view(http_method_names=['get']), name='Create'),
    path('create', PostCreateAndList.as_view(http_method_names=['post']), name='Create'),
    path('<int:pk>/', PostUpdateAndDelete.as_view(), name='Update And Delete'),
    path('<int:pk>/toggle/', PostLikeToggle.as_view(), name='Like Toggle'),
]