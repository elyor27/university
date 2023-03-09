from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path('create/', NewsCreateViews.as_view(), name='create'),
    path('delete/<int:pk>/', NewsDeleteViews.as_view(), name='delete'),
    path('Update/<int:pk>/', NewsUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', NewsDateilViews.as_view(), name='detail'),
    path('', NewsListViews.as_view(), name='list')
]